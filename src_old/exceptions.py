"""Exceptions for secfilr."""


class SECfilrError(Exception):
    """Base Exception for secfilr errors."""
    pass


class DataError(SECfilrError):
    """Raised when the client fails to read data."""
    pass


class DownloadError(SECfilrError):
    """Raised when an attempted download fails."""
    pass


class InvalidArgumentError(SECfilrError):
    """Raised when an invalid argument is passed."""
    pass


class JSONDecodingError(SECfilrError):
    """Raised when a JSON file cannot be properly decoded or validated."""
    pass


class MissingCredentialError(SECfilrError):
    """Raised when a required API credential is missing."""
    pass


class ParsingError(SECfilrError):
    """Raised when parsing fails."""
    pass


class RequestError(SECfilrError):
    """Raised when a request fails or encounters an error."""
    pass

