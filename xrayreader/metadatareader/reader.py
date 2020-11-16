"""
Class for reading metadata from xray datasets
"""
import glob
import os.path


class ReaderBase:
    """
    Store the filenames into a list.
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

        :return: list of filenames
        :rtype: list
        """
        if self.folder:
            self.filenames = glob.glob(self.folder)
        return self.filenames

    def parse_files(self):
        """
        Store patient data(age, gender, report) in a list 'data_china'.

        :return: list of metadata of the patient - filename,gender,age,true(has tb) or false, normal or not.
        :rtype: list
        """
