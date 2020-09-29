"""
XRay Image Container
"""

import os.path


class Image: #pylint: disable=too-few-public-methods
    """
    Image file data
    """
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        abspath_file = os.path.abspath(self.filename)
        self.path, _imagename = os.path.split(abspath_file)
        self.imagename, self.extension = os.path.splitext(_imagename)
        if self.extension[0] == '.':
            self.extension = self.extension[1:]

    def __str__(self):
        return f"Image: {self.imagename} - Format: {self.extension}"
