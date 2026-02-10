"""Dataclasses representing intermediate structures of SEC filing data.

These classes provide containers for companyfacts and concepts.
Used by SECfilr and ConceptParser.
"""

import json
from dataclasses import dataclass, field

import pandas as pd
from pydantic import BaseModel, Field, ValidationError

from secfilr.exceptions import InvalidArgumentError, JSONDecodingError


class CompanyCIK(BaseModel):
    """Container for company CIK data."""
    cik: int = Field(alias='cik_str')
    ticker: str
    title: str

    def __repr__(self) -> str:
        return f"CompanyFacts(ticker='{self.ticker}')"


def decode_cik_json(json_str: str, ticker: str) -> CompanyCIK:
    """Decode CIK JSON text into pydantic based container."""
    ticker_lower = ticker.lower()

    try:
        raw: dict[str, dict] = json.loads(json_str)
    except json.JSONDecodeError as e:
        raise JSONDecodingError('Error decoding CIK JSON') from e

    for entry in raw.values():
        if entry.get('ticker', '').lower() == ticker_lower:
            try:
                return CompanyCIK.model_validate(entry)
            except ValidationError as e:
                raise JSONDecodingError('Error validating CIK JSON') from e

    raise InvalidArgumentError(f'{ticker} Not found in CIK mapping data')


class Facts(BaseModel):
    """Raw SEC EDGAR filing data (JSON format)."""
    concepts: dict = Field(alias='us-gaap')

    def __len__(self) -> int:
        return len(self.concepts)


class CompanyFacts(BaseModel):
    """Container for pre-parsed data from SEC EDGAR.

    Ensures type and shape of SEC EDGAR JSON reponse with pydantic.
    """
    cik: int
    name: str = Field(alias='entityName')
    facts: Facts

    def __repr__(self) -> str:
        return f"CompanyFacts(name='{self.name}')"


def decode_companyfacts_json(json_str: str) -> CompanyFacts:
    """Decode companyfacts JSON text into pydantic based container."""
    try:
        return CompanyFacts.model_validate_json(json_str)
    except ValidationError as e:
        raise JSONDecodingError('Error validating companyfacts JSON') from e


def _normalize_financial_df(
    df: pd.DataFrame,
    value_col: str = 'val',
    date_col: str = 'date'
) -> pd.DataFrame:
    """Normalize shape for all DataFrames.

    - Converts `date_col` to datetime.date
    - Sorts rows by date
    - Drop NA dates and duplicate frames (if present)
    - Ensures `value_col` is float type
    - Moves `value_col` to the last column
    """
    df = df.copy()

    df[date_col] = pd.to_datetime(df[date_col], errors='coerce').dt.date
    df.dropna(subset=[date_col], inplace=True)
    df.sort_values(date_col, inplace=True)

    # Handle duplicates if frame exists
    if 'accn' in df.columns:
        df.drop_duplicates('accn', keep='last', inplace=True)

    df.reset_index(drop=True, inplace=True)
    df[value_col] = df[value_col].astype(float)

    # Ensure value column is last
    column_order = [c for c in df.columns if c != value_col] + [value_col]
    df = df.reindex(columns=column_order)

    return df


@dataclass
class Concept:
    """Container for parsed filings and metadata."""
    label: str = ''
    description: str = ''
    unit: str = ''
    filings: list[dict] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"Concept(label='{self.label}', unit='{self.unit}')"

    def __len__(self) -> int:
        return len(self.filings)

    def to_dataframe(self) -> pd.DataFrame:
        """Format Concept filings into pandas DataFrame.

        Returns:
            pd.DataFrame: of Concept filings
        """
        concept_df = pd.DataFrame(self.filings)
        return _normalize_financial_df(
            df = concept_df,
            value_col = 'val',
            date_col = 'filed'
        )


@dataclass
class CompanyConcept:
    """Container for parsed and sorted companyfacts data."""
    ticker: str
    name: str
    concept: Concept

    def __repr__(self) -> str:
        return f"CompanyFacts(ticker='{self.ticker}')"

