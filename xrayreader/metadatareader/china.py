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

        :return: gender, age
        :rtype: string, int
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
    def check_normality(file):
        """
        Indicates whether the patient has TB or not,
        or if it is a case of missing data.

        :return: `True` if the patient has tb, `False` otherwise
        :rtype: bool
        """
        try:
            flag = int(re.findall(r'_(\d).txt', file)[0])
            return[False, True][flag]
        except (ValueError, IndexError):
            pass
        return None



    def parse_files(self):
        """
        Stores patient data (age, gender, report) in a list 'data_montgomery'.

        :return: list of metadata (gender, age, filename, `True` if has tb, report) of the patients
        :rtype: list
        """
        data_china = {}
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
                        check_normality =self.check_normality(file),
                        report=report)
                data_china[xray.imagename] = xray
        return data_china
