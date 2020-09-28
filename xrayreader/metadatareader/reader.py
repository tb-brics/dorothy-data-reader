"""
Class for reading metadata from xray datasets
"""

import glob


class Reader:
    """
    This class returns the name of the file containing the x-ray image,
    the gender, the age and then the report of the patient
    """
    def __init__(self, **kwargs):
        """
        Construct the necessary attributes for the file to be read.
        Parameters
          age: int
              age of the patient
          gender: str
              gender of the patient
          filename: str
              the name of the file of the report
          report: str
              returns the report of the patient
        """
        self.age = kwargs.get('age', None)
        self.gender = kwargs.get('gender', None)
        self.filename = kwargs.get('filename', None)
        self.report = kwargs.get('report', None)

    def __str__(self):
        return f"<{self.filename}>:{self.gender}-{self.age} years - {self.report}"
