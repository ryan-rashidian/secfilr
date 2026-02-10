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
        self._parser = _ParseMetric(self.facts.concepts)
        self.ticker = ticker.strip().upper()
        self.name = companyfacts.name

    def concept(self, concept: str) -> dict | None:
        """Get raw concept."""
        if concept in self.facts.concepts:
            return self.facts.concepts[concept]
        else:
            return None

    def metric(self, metric: str) -> Metric:
        """Get parsed metric."""
        return self._parser.parse(metric)

    def statement(self, statement: str):
        """Get parsed statements."""
        pass

