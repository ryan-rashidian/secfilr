"""Contains the `Company` class.

`Company` serves as the main interface between the API user,
and any processing and parsing that secfilr may do.
"""

from secfilr.fetch import Fetch
from secfilr._models import CompanyFacts, Facts, Metric
from secfilr._parse import ParseMetric as _ParseMetric


class Company:
    """Main interface for secfilr.

    Args:
        ticker (str): company ticker symbol
        fetcher (Fetch): data fetcher
    """

    def __init__(self, ticker: str, fetcher: Fetch):
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
        return parser.parse(metric)

    def statement(self, statement: str):
        """Get parsed statements.

        PLACEHOLDER
        """
        pass

