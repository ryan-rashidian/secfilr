"""Main client for secfilr.

Orchestrates each step of:
- Fetching data
- Parsing data
- Mapping concepts
- Normalizing data shape
"""

import pandas as pd

from secfilr import _mappings
from secfilr.exceptions import InvalidArgumentError, ParsingError
from secfilr.fetcher import FactsLoader
from secfilr.parser import ConceptParser
from secfilr.schemas import (
    CompanyFacts,
    Concept,
    Facts,
    CompanyConcept,
)


class SECfilr:
    """Main client for secfilr."""

    def __init__(self, ticker: str):
        """Initialize data pipeline for given company.

        Args:
            ticker (str): Company ticker symbol
        """
        raw_companyfacts: CompanyFacts = FactsLoader(ticker).get_companyfacts()
        self.raw_facts: Facts = raw_companyfacts.facts
        self.parser = ConceptParser(self.raw_facts.concepts)
        self.ticker = ticker.strip().upper()
        self.name = raw_companyfacts.name

    def __repr__(self) -> str:
        return f'SECfilr({self.ticker})'

    def __str__(self) -> str:
        return f'[SECfilr]: ticker = {self.ticker} | name = {self.name}'

    def __bool__(self) -> bool:
        return bool(self.raw_facts)

    def _get_mappings(self, concept: str) -> tuple[str]:
        """Get matching tuple for concept mapping.

        Args:
            concept (str): Key for matching concept tuple
        Returns:
            tuple[str]: Matching concept mapper
        Raises:
            InvalidArgumentError: If undefined concept key is given
        """
        try:
            section, label = _mappings.map_arg[concept.lower()]
            return _mappings.filing_tags[section][label]
        except KeyError as e:
            raise InvalidArgumentError(f'{concept} is undefined') from e

    def get_concept(self, concept: str) -> CompanyConcept:
        """Get parsed filing data for given concept.

        Args:
            concept (str): Key for matching concept mapper
        Returns:
            CompanyConcept: Containing concept data
        """
        xbrl_mappings = self._get_mappings(concept)
        parsed_concept: Concept = self.parser.parse(xbrl_mappings)
        return CompanyConcept(
            ticker = self.ticker,
            name = self.name,
            concept = parsed_concept
        )

    def get_all_concepts(self) -> dict[Concept, None]:
        """Get all concepts from filing data.

        Returns:
            dict[Concept, None]: Containing data for all concepts
        """
        concepts_dict = {}
        for concept in _mappings.map_arg.keys():
            if concept not in concepts_dict.keys():
                try:
                    xbrl_mappings = self._get_mappings(concept)
                    parsed_concept: Concept = self.parser.parse(xbrl_mappings)
                    concepts_dict[concept] = parsed_concept
                except ParsingError:
                    concepts_dict[concept] = None
        return concepts_dict

    def _get_latest_statement(self, section: str) -> list[tuple]:
        """Build a DataFrame of a statement from parsed concepts"""
        statement = []
        filed, form = None, None

        for concept, xbrl_mappings in _mappings.filing_tags[section].items():
            try:
                parsed_data: Concept = self.parser.parse(xbrl_mappings)
                latest_filing: dict = parsed_data.filings[-1]
                value = latest_filing.get('val')
                form = latest_filing.get('form')
                filed = latest_filing.get('filed')
                statement.append((concept, value))
            except ParsingError:
                statement.append((concept, None))
        statement.append(('Filed', filed))
        statement.append(('Form', form))

        return statement

    def get_balance_sheet_df(self) -> pd.DataFrame:
        """Get DataFrame of latest balance sheet."""
        balance_sheet = self._get_latest_statement('Balance Sheet')
        balance_sheet_df = pd.DataFrame(balance_sheet)
        balance_sheet_df.columns = ['Metric', 'val']
        return balance_sheet_df

    def get_cashflow_statement_df(self) -> pd.DataFrame:
        """Get DataFrame of lastest cashflow statement."""
        cashflow_statement = self._get_latest_statement('Cash Flow Statement')
        cashflow_statement_df = pd.DataFrame(cashflow_statement)
        cashflow_statement_df.columns = ['Metric', 'val']
        return cashflow_statement_df

    def get_income_statement_df(self) -> pd.DataFrame:
        """Get DataFrame of lastest income stament."""
        income_statement = self._get_latest_statement('Income Statement')
        income_statement_df = pd.DataFrame(income_statement)
        income_statement_df.columns = ['Metric', 'val']
        return income_statement_df

