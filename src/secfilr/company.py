"""Contains the `Company` class.

`Company` serves as the main interface between the API user,
and any processing and parsing that secfilr may do.
"""

from enum import StrEnum

from secfilr import _xbrl_labels
from secfilr._models import CompanyFacts, Facts, Metric
from secfilr._parse import ParseMetric as _ParseMetric
from secfilr.exceptions import InvalidMetric, ParsingError
from secfilr.fetch import Fetch


class StatementType(StrEnum):
    """Enumerations for statment keys."""
    BALANCE_SHEET = 'Balance Sheet'
    CASH_FLOW_STATEMENT = 'Cash Flow Statement'
    INCOME_STATEMENT = 'Income Statement'


class Company:
    """Main interface for secfilr.

    Args:
        ticker (str): company ticker symbol
        fetcher (Fetch): data fetcher
    """

    def __init__(self, ticker: str, fetcher: Fetch) -> None:
        """Initialize companyfacts and parser using given fetcher."""
        companyfacts: CompanyFacts = fetcher.companyfacts(ticker)
        self.facts: Facts = companyfacts.facts
        self.ticker = ticker.strip().upper()
        self.name = companyfacts.name

    def __repr__(self) -> str:
        return f'SECfilr({self.ticker})'

    def __str__(self) -> str:
        return f'[SECfilr]: ticker = {self.ticker} | name = {self.name}'

    def concept(self, concept: str) -> dict | None:
        """Get a raw concept.

        Args:
            concept (str)
        Returns:
            Dict: of filings for concept
            None: if concept is not found
        """
        if concept in self.facts.concepts:
            return self.facts.concepts[concept]
        else:
            return None

    def _get_metric_mapper(self, metric: str) -> tuple[str]:
        """Get matching tuple for metric mapping."""
        try:
            section, label = _xbrl_labels.map_arg[metric]
            return _xbrl_labels.statements[section][label]
        except KeyError as e:
            raise InvalidMetric(f'{metric} is undefined') from e

    def metric(self, metric: str) -> Metric:
        """Get a parsed metric.

        Args:
            metric (str)
        Returns:
            Metric: dataclass for filings
        Raises:
            ParseError: if parsing fails
        """
        parser = _ParseMetric(self.facts.concepts)
        xbrl_mapping = self._get_metric_mapper(metric.lower())
        return parser.parse(xbrl_mapping)

    def statement(
        self,
        statement_t: StatementType,
        quarter_off: int = 0
    ) -> dict:
        """Build a statement from parsed metrics."""
        parser = _ParseMetric(self.facts.concepts)
        statement_dict = {}
        filed, form = None, None

        for concept, labels in _xbrl_labels.statements[statement_t].items():
            try:
                parsed_metric: Metric = parser.parse(labels)
                latest_filing: dict = parsed_metric.filings[-(quarter_off+1)]
                value = latest_filing.get('val')
                form = latest_filing.get('form')
                filed = latest_filing.get('filed')
                statement_dict[concept] = value
            except ParsingError:
                statement_dict[concept] = None
        statement_dict['filed'] = filed
        statement_dict['form'] = form

        return statement_dict

