"""Contains the `Downloader` class for downloading bulk filing data."""

import json
import pathlib
import shutil
import zipfile

from ._network import download_files as _download_files
from ._network import make_request as _make_request
from ._urls import EDGAR_CIK_URL, EDGAR_ZIP_URL


class Downloader:
    """Bulk filing data downloader."""

    def __init__(self, user_agent: str, dest_path: pathlib.Path):
        """Initialize paths.

        Args:
            user_agent (str): EDGAR API user-agent credential
            dest_path (Path): destination directory for bulk data
        """
        # Build paths from dest_path root
        self.path_dest_dir = dest_path / 'bulk_data'
        self.path_dest_dir.mkdir(exist_ok=True)
        self.path_facts_zip = self.path_dest_dir / 'companyfacts.zip'
        self.path_facts_unzipped = self.path_dest_dir / 'companyfacts'
        self.path_tickers_json = self.path_dest_dir / 'company_tickers.json'
        # Build EDGAR API header
        self.headers = {'User-Agent': user_agent}

    def _download_cik_mapping(self) -> None:
        """Download CIK file for mapping ticker symbols."""
        cik_data = _make_request(
            url=EDGAR_CIK_URL,
            headers=self.headers
        )
        with open(self.path_tickers_json, 'w') as f:
            json.dump(json.loads(cik_data), f)

    def _download_companyfacts_zip(self) -> None:
        """Download the bulk companyfacts zip file."""
        _download_files(
            url = EDGAR_ZIP_URL,
            headers = self.headers,
            dest_path = self.path_dest_dir
        )

    def _unzip_companyfacts(self) -> None:
        """Un-zip companyfacts."""
        with zipfile.ZipFile(self.path_facts_zip, 'r') as zip:
            zip.extractall(self.path_facts_unzipped)

    def remove(self) -> None:
        """Remove all bulk data files."""
        for path in [
            self.path_tickers_json,
            self.path_facts_zip,
            self.path_facts_unzipped
        ]:
            if path.exists():
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()

    def download(self) -> None:
        """Download CIK mapping, bulk files, and unzip companyfacts."""
        self._download_cik_mapping()
        self._download_companyfacts_zip()
        self._unzip_companyfacts()

