# secfilr

> [!WARNING]
> **WORK IN PROGRESS**: Everything is subject to change.

Python API for SEC EDGAR.

## Features

- Pythonic API for accessing SEC EDGAR filings
- Choice between using requests, or bulk-data as the data source
- Mapping of GAAP concepts into generalized, named 'metric' categories

## Installation

```bash
git clone https://github.com/ryan-rashidian/secfilr
cd secfilr
pip install .
```

## Usage

Documentation and examples are planned.

## To-Do

- Better exceptions and handling of parsing failure: either make it clear why the failure occurred, or simply return `Thing | None`.
- Re-implement statements.

