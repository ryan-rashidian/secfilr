# secfilr - Python wrapper for SEC EDGAR API

**Work in Progress**

Use SEC EDGAR as a proper Python API with built-in parsing.

## Features

- Pythonic API for accessing SEC EDGAR filings
- Choice between using requests, or bulk-data as the data source
- Mapping of GAAP concepts into generalized, named categories

## Installation

```bash
git clone https://github.com/ryan-rashidian/secfilr
cd secfilr
pip install .
```

## Usage

(Temporary Usage Guide):

- Install secfilr (in a venv for example)
- Use the `write_credential` function to enter a `EDGAR_USER_AGENT`
    e.g. `write_credential('john johndoe@example.com')`
- `refresh_bulk_data()` function call will download the SEC's bulk-data
- `clean_secfilr()` function call removes/deletes credentials and bulk-data
- `SECfilr` class is the main client for the wrapper

platformdirs library is used to locate a user's data and config directory,
secfilr will create 2 directories on your file-system, one in each:
The /secfilr/ directory in the data directory is for bulk-data.
The /secfilr/ directory in the config directory is for API credentials.

Since these directories are independent of a single package install,
they can be used across multiple installations of secfilr,
and must also be removed separately (manually, or call `clean_secfilr()`).

Documentation and examples are planned.
For now, refer to the docstrings in the source code.

