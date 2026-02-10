"""Networking utilities for secfilr."""

from pathlib import Path

import requests

from secfilr.exceptions import DownloadError, RequestError


def make_request(
    url: str,
    headers: dict[str, str] | None = None,
    params: dict[str, str] | None = None
) -> str:
    """Make a request wrapped with error handling.

    Args:
        url (str): request URL
        headers (dict[str, str]): request headers
        params (dict[str, str]): request parameters

    Returns:
        str: encoded JSON text as string

    Raises:
        RequestError: if request fails
    """
    try:
        response = requests.get(url=url, headers=headers, params=params)
        response.raise_for_status()
        return response.text

    except requests.exceptions.HTTPError as e:
        raise RequestError('HTTP Error') from e
    except requests.exceptions.RequestException as e:
        raise RequestError('Request Error') from e
    except Exception as e:
        raise RequestError('Unexpected request Error') from e


def download_files(
    url: str,
    dest_path: Path,
    headers: dict[str, str] | None = None
) -> None:
    """File downloader wrapped with error handling.

    Args:
        url (str): request URL
        headers (dict[str, str]): request headers
        dest_path (pathlib.Path): download path destination

    Raises:
        DownloadError: if attempted download fails
    """
    try:
        with requests.get(url=url, headers=headers, stream=True) as r:
            r.raise_for_status()
            with open(dest_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

    except requests.exceptions.HTTPError as e:
        raise DownloadError('HTTP Error') from e
    except requests.exceptions.RequestException as e:
        raise DownloadError('Request Error') from e
    except Exception as e:
        raise DownloadError('Unexpected request Error') from e

