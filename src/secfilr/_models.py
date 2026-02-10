"""Container objects for secfilr.

Pydantic models based on the shape of JSON filing data from SEC EDGAR.
`Concept` dataclass for parsed metric
"""

from dataclasses import dataclass, field
import json

from pydantic import BaseModel, Field, ValidationError

from secfilr.exceptions import FileDecodeError, TickerNotFound


class CompanyCIK(BaseModel):
    """Container for company CIK data."""
    cik: int = Field(alias='cik_str')
    ticker: str
    title: str


def decode_cik_json(json_str: str, ticker: str) -> CompanyCIK:
    """Decode CIK JSON text into pydantic based container."""
    ticker_lower = ticker.lower()

    try:
        raw: dict[str, dict] = json.loads(json_str)
    except json.JSONDecodeError as e:
        raise FileDecodeError('Error decoding CIK JSON') from e

    for entry in raw.values():
        if entry.get('ticker', '').lower() == ticker_lower:
            try:
                return CompanyCIK.model_validate(entry)
            except ValidationError as e:
                raise FileDecodeError('Error validating CIK JSON') from e
    raise TickerNotFound(f'{ticker} Not found in CIK mapping data')


class Facts(BaseModel):
    """Raw SEC EDGAR filing data."""
    concepts: dict = Field(alias='us-gaap')

    def __len__(self) -> int:
        return len(self.concepts)


class CompanyFacts(BaseModel):
    """Container for pre-parsed data from SEC EDGAR."""
    cik: int
    name: str = Field(alias='entityName')
    facts: Facts

    def __repr__(self) -> str:
        return f"CompanyFacts(cik={self.cik}, name='{self.name}')"


def decode_companyfacts_json(json_str: str) -> CompanyFacts:
    """Decode companyfacts JSON text into pydantic based container."""
    try:
        return CompanyFacts.model_validate_json(json_str)
    except ValidationError as e:
        raise FileDecodeError('Error validating companyfacts JSON') from e


@dataclass
class Metric:
    """Container for a parsed metric and metadata."""
    label: str
    description: str
    unit: str
    filings: list[dict] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"Metric(label='{self.label}')"

    def __len__(self) -> int:
        return len(self.filings)

