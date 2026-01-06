"""This module contains filesystem path(s) used by secfilr."""

from pathlib import Path

from platformdirs import user_config_path, user_data_path

APP_NAME = 'secfilr'


def _get_data_path() -> Path:
    """Returns the absolute Path object for data directory.

    If the directory does not exist, it will be created.
    """
    return user_data_path(
        appname = APP_NAME,
        roaming = False,
        ensure_exists = True
    )


def _get_config_path() -> Path:
    """Returns the absolute Path object for config directory.

    If the directory does not exist, it will be created.
    """
    return user_config_path(
        appname = APP_NAME,
        roaming = False,
        ensure_exists = True
    )


DATA_DIR = _get_data_path()
CONFIG_DIR = _get_config_path()

DOTENV_PATH: Path = CONFIG_DIR / '.env'
DOTENV_PATH.touch(exist_ok=True)

BULK_DATA_DIR: Path = DATA_DIR / 'bulkdata'
BULK_DATA_DIR.mkdir(parents=True, exist_ok=True)

COMPANYFACTS_ZIP: Path = BULK_DATA_DIR / 'companyfacts.zip'
COMPANYFACTS_UNZIPPED: Path = BULK_DATA_DIR / 'companyfacts'
COMPANY_TICKERS_JSON: Path = BULK_DATA_DIR / 'company_tickers.json'

