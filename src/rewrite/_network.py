"""Networking utilities for secfilr using requests library."""

from pathlib import Path

import requests

from .exceptions import DownloadError, RequestError


def make_request(
    url: str,
    headers: dict[str, str] | None = None,
    params: dict[str, str] | None = None
) -> str:
    """Make a request wrapped with error handling."""
    try:
        response = requests.get(url=url, headers=headers, params=params)
        response.raise_for_status()
        return response.text
    except Exception as e:
        raise RequestError('Error encountered during request') from e


def download_files(
    url: str,
    dest_path: Path,
    headers: dict[str, str] | None = None
) -> None:
    """File downloader wrapped with error handling."""
    try:
        with requests.get(url=url, headers=headers, stream=True) as r:
            r.raise_for_status()
            with open(dest_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    except Exception as e:
        raise DownloadError('Error encountered during download') from e

