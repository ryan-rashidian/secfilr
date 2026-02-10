"""Companyfacts data fetching."""

from abc import ABC, abstractmethod
from pathlib import Path

from secfilr._network import make_request
from secfilr._urls import EDGAR_CIK_URL, EDGAR_FACTS_URL
from secfilr.exceptions import FetchError
from secfilr._models import (
    CompanyCIK,
    CompanyFacts,
    decode_cik_json,
    decode_companyfacts_json,
)


class Fetch(ABC):
    """Base class for companyfact fetchers."""

    @abstractmethod
    def companyfacts(self, ticker: str) -> CompanyFacts:
        pass


class FetchBulk(Fetch):
    """Fetch from bulk filing data.

    Args:
        company_tickers (Path): path to company_tickers.json
        companyfacts_dir (Path): path to companyfacts directory
    """

    def __init__(
        self,
        company_tickers: Path,
        companyfacts_dir: Path
    ):
        """Initialize paths."""
        self.company_tickers = company_tickers
        self.companyfacts_dir = companyfacts_dir

    def _load_json(self, path: Path) -> str:
        """Load JSON file with error handling."""
        try:
            with open(path, 'r') as f:
                return f.read()

        except Exception as e:
            raise FetchError(f'Error reading: {path.resolve()}') from e

    def companyfacts(self, ticker: str) -> CompanyFacts:
        """Fetch companyfacts for given ticker symbol."""
        ticker_fmt = ticker.strip().lower()
        cik_json = self._load_json(self.company_tickers)
        cik_data: CompanyCIK = decode_cik_json(cik_json, ticker=ticker_fmt)
        cik = str(cik_data.cik).zfill(10)
        companyfacts_file = self.companyfacts_dir / f'CIK{cik}.json'
        companyfacts_json: str = self._load_json(companyfacts_file)
        return decode_companyfacts_json(companyfacts_json)


class FetchRequest(Fetch):
    """Fetch using a request to SEC EDGAR.

    Args:
        user_agent (str): EDGAR API User-Agent
    """

    def __init__(self, user_agent: str):
        """Initialize headers."""
        self.headers = {'User-Agent': user_agent}

    def companyfacts(self, ticker: str) -> CompanyFacts:
        """Fetch companyfacts for given ticker symbol."""
        ticker_fmt = ticker.strip().lower()
        cik_json: str = make_request(url=EDGAR_CIK_URL, headers=self.headers)
        cik_data: CompanyCIK = decode_cik_json(cik_json, ticker=ticker_fmt)
        cik = str(cik_data.cik).zfill(10)
        cik_facts_url = f'{EDGAR_FACTS_URL}CIK{cik}.json'
        companyfacts_json: str = make_request(
            url=cik_facts_url,
            headers=self.headers
        )
        return decode_companyfacts_json(companyfacts_json)

