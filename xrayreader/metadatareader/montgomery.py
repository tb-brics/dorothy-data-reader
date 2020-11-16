"""
Class for reading metadata from files of the Montgomery Dataset.
"""

import re
from .reader import ReaderBase
from .xray_image_metadata import XRayImageMetadata


class Reader(ReaderBase):
    """
    Normally the first line is something like:
    <Patient's Sex: (the first letter of the gender, like F or M)>
    the second line:
    <Patient's Age: (number with 3 digits Y)>
    the third line:
    <report>

    Attributes
    ----------
    gender: str
      gender of the patient
    age: int
      age of the patient
    report: str
      gives the report of the patient

    Methods
    -------
    patient_gender(firstline)
        Return the gender of the patient.

    patient_age(secondline)
        Return the age of the patient.

    check_normality(file)
        Indicate if the patient has tb or not.

    parse_files(self)
        Stores patient data in a list.
    """

    @staticmethod
    def patient_gender(firstline):
        """
        Return the gender of the patient.

        :return: gender
        :rtype: string
        """
        gender = None
        if 'F' in firstline:
            gender = 'female'
        elif 'M' in firstline:
            gender = 'male'
        return gender

    @staticmethod
    def patient_age(secondline):
        """
        Return the age of the patient.

        :return: age
        :rtype: int
        """
        try:
            age = int(re.findall(r'\d+', secondline)[0])
        except IndexError:
            age = None
        return age

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
        data_montgomery = []
        for file in self.get_filenames():
            with open(file) as txtfile:
                content = txtfile.read()
                lines = content.split('\n')
                lines = [l.strip() for l in lines]
                gender = self.patient_gender(lines[0])
                age = self.patient_age(lines[1])
                report = lines[2]
                xray = XRayImageMetadata(gender=gender,
                                         age=age,
                                         filename=file,
                                         check_normality =self.check_normality(file),
                                         report=report)
                data_montgomery.append(xray)
        return data_montgomery
