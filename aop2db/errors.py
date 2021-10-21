"""Project defined errors."""

dl_error = """Passed string argument must be either:\n
        1. A single GEO series ID (string)\n
        2. A comma separated list of GEO series IDs (string)\n
        3. A path to a file containing GEO series IDs (string)\n
        4. A list of GEO series IDs (Iterable)"""


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class DownloadError(Error):
    """Exception raised for errors in the download CLI method."""

    def __init__(self, message=dl_error):
        self.message = message
        super().__init__(self.message)
