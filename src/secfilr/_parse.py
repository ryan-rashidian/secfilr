"""Metric Parser.

Parse concepts into categorized metrics defined by secfilr.
"""

from secfilr._models import Metric
from secfilr.exceptions import ParsingError


class ParseMetric:
    """Metric parser."""

    def __init__(self, raw_facts: dict) -> None:
        """Initialize raw companyfacts data."""
        self.raw_facts = raw_facts

    def _map_to_metric(self, xbrl_mappings: tuple[str]) -> dict:
        """Map XBRL labels to categorized metric."""
        for map in xbrl_mappings:
            if map not in self.raw_facts:
                continue
            return self.raw_facts[map]
        raise ParsingError('Mapping: No matches found.')

    def _get_units(self, units_dict: dict | None) -> str:
        """Get unit key for concept."""
        if not units_dict:
            raise ParsingError('Filing data not found.')
        return next(iter(units_dict))

    def parse(self, xbrl_mapping: tuple[str]) -> Metric:
        """Get parsed Concept from an xbrl_mapping."""
        concept: dict = self._map_to_metric(xbrl_mapping)
        label: str = concept.get('label', '')
        description: str = concept.get('description', '')
        unit: str = self._get_units(concept.get('units'))
        concept_files: list = concept['units'][unit]
        # Avoid duplicate filings
        concept_files_parsed = [
            f for f in concept_files if 'frame' in f.keys()
        ]
        return Metric(
            label = label,
            description = description,
            unit = unit,
            filings = concept_files_parsed
        )

