"""Test and demo."""

from pathlib import Path

from secfilr.fetch import FetchBulk
from secfilr.company import Company, Metric
from secfilr.company import StatementType as stmnt

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
    print(f'{assets.label}: {assets.description}')
    print('\nFILING DATA:')
    recent_filing: dict = assets.filings[-1]
    for key, value in recent_filing.items():
        print('----------')
        print(key)
        print(value)
    print('----------')

    balance_sheet: dict = aapl.statement(
        statement_t = stmnt.BALANCE_SHEET,
        quarter_off = 0 # Quarter offset `0`; most recent statement
    )
    print('\nBALANCE SHEET:')
    for metric, value in balance_sheet.items():
        print('----------')
        print(metric)
        print(value)
    print('----------')


if __name__ == '__main__':
    main()

