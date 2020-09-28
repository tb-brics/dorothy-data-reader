"""
Get images from India DataSet
"""

from .reader import ReaderBase
import os.path


class Reader(ReaderBase):
    """
    Get images from image data set
    """
    suffix = "*/*"

    def __init__(self, **kwargs):
        """
        Initial method
        """
        dataset = kwargs.get("dataset", "DatasetA")
        path = kwargs.get("path")
        if path:
            path = os.path.join(path, dataset)

        super(Reader, self).__init__(path=path)

