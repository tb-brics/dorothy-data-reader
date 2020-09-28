"""
Base class for parsing xray image files in a directory
"""

from .xray_image import Image
import glob
import os.path


class ReaderBase:
    """
    This class stores the filenames into a list.
    """
    suffix = "*"

    def __init__(self, **kwargs):
        self.folder = None
        path = kwargs.get("path")
        if path:
            self.folder = os.path.join(path, self.suffix)

    def get_filenames(self):
        """
        Return the name of the file in which the report is stored.
        """
        if self.folder: 
            filenames = glob.glob(self.folder)
        return filenames

    def get_images(self):
        return [Image(filename=f) for f in self.get_filenames()]
