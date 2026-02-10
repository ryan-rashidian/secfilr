"""Exceptions for secfilr."""


class SECfilrError(Exception):
    """Base Exception for secfilr errors."""
    pass


class NetworkError(SECfilrError):
    """Raised when a request fails."""
    pass


class FileDecodeError(SECfilrError):
    """Raised when a JSON file fails to be load or validated."""
    pass


class TickerNotFound(SECfilrError):
    """Raised when no CIK can be found for a given ticker symbol."""
    pass


class RequestError(SECfilrError):
    """Raised when a request encounters an error."""
    pass


class DownloadError(SECfilrError):
    """Raised when a download encounters an error."""
    pass


class FetchError(SECfilrError):
    """Raised when an error occurs while fetching filing data."""
    pass


class ParsingError(SECfilrError):
    """Raised when the parsing of a file fails."""
    pass


class InvalidMetric(SECfilrError):
    """Raised when an invalid metric string is given as an argument."""
    pass

