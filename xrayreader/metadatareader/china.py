"""
Class for reading metadata from files of the China Dataset
"""

import re
from .reader import ReaderBase
from .xray_image_metadata import XRayImageMetadata

class Reader(ReaderBase):
    """
    A class to read the file and return the report.

    Attributes
    ----------
    gender: str
      gender of the patient
    age: int
      age of the patient
    report: str
      gives the report of the patient
    """
    @staticmethod
    def clear_firstline(firstline):
        """
        Normally the first line is something like:
        <gender> <age>yrs
        """
        firstline = firstline.lower()
        gender = None
        if 'female' in firstline:
            gender = 'female'
        else:
            if 'male' in firstline:
                gender = 'male'
        try:
            age = int(re.findall(r'\d+', firstline)[0])
        except IndexError:
            age = None
        return gender, age

    @staticmethod
    def has_tb(report):
        """
        Indicates whether the patient has TB or not,
        or if it is a case of missing data.
        """
        if not report:
            return None
        return report.strip() != 'normal'

    def parse_files(self):
        data_china = []
        for file in self.get_filenames():
            with open(file) as txtfile:
                content = txtfile.read()
                lines = content.split('\n')
                lines = [l.strip() for l in lines]
                gender, age = self.clear_firstline(lines[0])
                report = lines[1]
                xray = XRayImageMetadata(gender=gender,
                        age=age,
                        filename=file,
                        has_tb= self.has_tb(report),
                        report=report)
                data_china.append(xray)
        return data_china
