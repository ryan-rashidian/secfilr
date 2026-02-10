"""Metric Parser.

Parse concepts into categorized metrics defined by secfilr.
"""

from secfilr import _xbrl_labels
from secfilr.exceptions import ParsingError, InvalidMetric
from secfilr._models import Metric


class ParseMetric:
    """Metric parser."""

    def __init__(self, raw_facts: dict):
        """Initialize raw companyfacts data."""
        self.raw_facts = raw_facts

    def _get_mappings(self, metric: str) -> tuple[str]:
        """Get matching tuple for concept mapping."""
        try:
            section, label = _xbrl_labels.map_arg[metric]
            return _xbrl_labels.filing_tags[section][label]
        except KeyError as e:
            raise InvalidMetric(f'{metric} is undefined') from e

    def _map_to_metric(self, xbrl_mappings: tuple[str]) -> dict:
        """Map XBRL labels to categorized metric."""
        for map in xbrl_mappings:
            if map not in self.raw_facts:
                continue
            return self.raw_facts[map]
        raise ParsingError('Mapping: No matches found.')

    def _get_units(self, units_dict: dict | None) -> str:
        """Get unit key value for concept."""
        if not units_dict:
            raise ParsingError('Filing data not found.')
        return next(iter(units_dict))

    def parse(self, metric: str) -> Metric:
        """Get parsed Concept from an xbrl_mapping."""
        xbrl_mapping = self._get_mappings(metric.lower())
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

