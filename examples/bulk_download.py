"""Bulk filing download script.

Removes old files (if they exist) and downloads new bulk data.
"""

from os import getenv
from pathlib import Path
from secfilr.downloader import Downloader


# Path to where bulkdata directory should be created (or already exists)
BASE_PATH = Path('/path/to/dir')


def main():
    """Remove old files and download new bulk data."""
    # In this example, the `User-Agent` is stored as an env var
    user_agent = getenv('API_EDGAR_USERAGENT')
    if not user_agent:
        print('API_EDGAR_USERAGENT environment variable not found')
        return None

    downloader = Downloader(user_agent, BASE_PATH)
    print('Removing old bulk data...')
    downloader.remove()
    print('Downloading bulk data.\nThis may take several minutes...')
    downloader.download()
    print('Download complete.')


if __name__ == '__main__':
    main()

