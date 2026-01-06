"""Bulk data download manager for secfilr.

Download or remove bulk filing data from SEC EDGAR.
Size: ~20GB
"""

from json import dump, loads
from shutil import rmtree
from zipfile import ZipFile

from secfilr._networking import download_files, make_request
from secfilr.config._paths import (
    BULK_DATA_DIR,
    COMPANY_TICKERS_JSON,
    COMPANYFACTS_UNZIPPED,
    COMPANYFACTS_ZIP,
)
from secfilr.config._urls import EDGAR_CIK_URL, EDGAR_ZIP_URL
from secfilr.config.credentials import require_credential


def _ensure_bulk_dir() -> None:
    """Ensure that the bulk_data directory exists."""
    BULK_DATA_DIR.mkdir(parents=True, exist_ok=True)


def _edgar_headers() -> dict[str, str]:
    """Return headers dict containing the EDGAR User-Agent."""
    cred = require_credential(service='EDGAR', env_var='EDGAR_USER_AGENT')
    return {'User-Agent': cred}


def download_cik_mapping() -> None:
    """SEC EDGAR company_tickers.json bulk data downloader.

    Contains CIK mapping data for all tickers.
    """
    _ensure_bulk_dir()
    headers = _edgar_headers()
    cik_data = make_request(url=EDGAR_CIK_URL, headers=headers)
    with open(COMPANY_TICKERS_JSON, 'w') as f:
        dump(loads(cik_data), f)


def download_companyfacts_zip() -> None:
    """SEC EDGAR companyfacts.zip bulk data downloader.

    Contains companyfacts.json for all companies by CIK.
    """
    _ensure_bulk_dir()
    headers = _edgar_headers()
    download_files(
        url = EDGAR_ZIP_URL,
        headers = headers,
        dest_path = COMPANYFACTS_ZIP
    )


def unzip_companyfacts() -> None:
    """Un-zip companyfacts.zip folder."""
    with ZipFile(COMPANYFACTS_ZIP, 'r') as zip:
        zip.extractall(COMPANYFACTS_UNZIPPED)


def delete_bulk_data() -> None:
    """Remove all existing SEC bulk data files and directories."""
    for path in [
        COMPANYFACTS_ZIP,
        COMPANYFACTS_UNZIPPED,
        COMPANY_TICKERS_JSON
    ]:
        if path.exists():
            if path.is_dir():
                rmtree(path)
            else:
                path.unlink()


def refresh_bulk_data() -> None:
    """Delete old data, download bulk files, and unzip companyfacts."""
    delete_bulk_data()
    download_cik_mapping()
    download_companyfacts_zip()
    unzip_companyfacts()

