"""Clean up and remove secfilr data from a machine."""

from shutil import rmtree

from secfilr.config._paths import DATA_DIR, CONFIG_DIR


def clean_secfilr() -> None:
    """Remove all extra secfilr data.

    - SEC bulk data filings
    - User API credentials
    """
    for path in [DATA_DIR, CONFIG_DIR]:
        if path.exists():
            if path.is_dir():
                rmtree(path)
            else:
                path.unlink()

