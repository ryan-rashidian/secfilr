"""API credentials and authentication for secfilr."""

import os
from typing import Optional, Tuple

from dotenv import load_dotenv, set_key, unset_key

from secfilr.config._paths import DOTENV_PATH
from secfilr.exceptions import MissingCredentialError

load_dotenv(dotenv_path=DOTENV_PATH)


def write_credential(value: str) -> None:
    """Write user-credentials to the .env file."""
    set_key(DOTENV_PATH, 'EDGAR_USER_AGENT', value)


def remove_credential(env_var: str) -> Tuple[Optional[bool], str]:
    """Remove user-credentials from the .env file."""
    return unset_key(DOTENV_PATH, env_var)


def require_credential(service: str, env_var: str) -> str:
    """Require user-credentials for access."""
    value = os.getenv(env_var)
    if not value:
        raise MissingCredentialError(
            f'{service} API credentials are not configured.'
        )
    return value

