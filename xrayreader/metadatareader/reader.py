"""
Class for reading metadata from xray datasets
"""
import glob
import os.path


class ReaderBase:
    """
    This class stores the filenames into a list.
    """
    suffix = "*"

    def __init__(self, **kwargs):
        path = kwargs.get("path")
        if path:
            self.folder = os.path.join(path, self.suffix)
        self.filenames = []

    def get_filenames(self):
        """
        Return the name of the file in which the report is stored.
        """
        if self.folder: 
            self.filenames = glob.glob(self.folder)
        return self.filenames

    def parse_files(self):
        """
        This function stores patient data(age, gender, report) in a list 'data_china'.
        """
        pass
