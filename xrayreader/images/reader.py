"""
Base class for parsing xray image files in a directory.
"""

import glob
import os.path
from .xray_image import Image


class ReaderBase:
    """
    Store the filenames into a list.

    Attributes
    ----------
    path: string
        Path where the images are stored.

    filename: string
        Name of the file in which the report is stored.

    Methods
    -------
    __init__(**kwargs)
        Initial method to get the path of the images.

    get_filenames
        Return the name of the files in which the reports are stored.

    get_images
        Return tha name of the images and the format of them.

    """
    suffix = "*"

    def __init__(self, **kwargs):
        self.folder = None
        path = kwargs.get("path")
        if path:
            self.folder = os.path.join(path, self.suffix)

    def get_filenames(self):
        """
        Return the name of the files in which the reports are stored.

        :return: list with the filenames
        :rtype: list
        """
        if self.folder:
            filenames = glob.glob(self.folder)
        return filenames

    def get_images(self):
        """
        Return the name of the images and the format of them.

        :return: list with the name of the images and the format of the image.
        :rtype: list
        """
        return [Image(filename=f) for f in self.get_filenames()]
