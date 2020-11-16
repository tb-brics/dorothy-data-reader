"""
Get data of the images from India DataSet.
"""

import os.path
from .reader import ReaderBase


class Reader(ReaderBase):
    """Get data of the images from image dataset."""
    suffix = "*/*"

    def __init__(self, **kwargs):
        """
        Initial method.

        Attributes
        ----------
        path: string
            Path of the image.

        dataset: string
            Name of the dataset.
        """
        dataset = kwargs.get("dataset", "DatasetA")
        path = kwargs.get("path")
        if path:
            path = os.path.join(path, dataset)
        super(Reader, self).__init__(path=path)
