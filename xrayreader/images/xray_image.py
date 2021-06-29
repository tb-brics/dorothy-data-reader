"""
XRay Image Container
"""

from ..utils import parse_filename

class Image: #pylint: disable=too-few-public-methods
    """
    Image file data
    """
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.path, self.imagename, self.extension = parse_filename(self.filename)

    def __str__(self):
        return f"Image: {self.imagename} - Format: {self.extension}"
