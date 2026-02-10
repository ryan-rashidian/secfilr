"""Test and demo."""

from pathlib import Path

from secfilr.fetch import FetchBulk
from secfilr.company import Company, Metric

BASE_PATH = Path('/path/to/bulkdata')


def main():
    """Test secfilr"""
    company_tickers = BASE_PATH / 'company_tickers.json'
    companyfacts_dir = BASE_PATH / 'companyfacts'

    fetcher = FetchBulk(
        company_tickers = company_tickers,
        companyfacts_dir = companyfacts_dir
    )
    aapl = Company('AAPL', fetcher)
    assets: Metric = aapl.metric('assets')

    print(aapl.ticker)
    print(aapl.name)
    print(assets.unit)
    print(assets.label)
    print(assets.description)
    print(assets.filings[0])


if __name__ == '__main__':
    main()

