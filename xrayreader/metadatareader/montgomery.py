"""
Class for reading metadata from files of the 
Montgomery Dataset
"""

from .reader import ReaderBase
from .xray_image_metadata import XRayImageMetadata
import re


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
    """

    @staticmethod
    def patient_gender(firstline):
        """
        Returns the gender of the patient.
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
        Returns the age of the patient.
        """
        try:
           age = int(re.findall(r'\d+', secondline)[0])
        except IndexError:
           age = None
        return age

    @staticmethod
    def has_tb(report):
        if not report:
            return None    
        return report.strip() != "normal"

    def parse_files(self):
        """
        Stores patient data (age, gender, report) in a list 'data_montgomery'.
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
                                         has_tb=self.has_tb(report),
                                         report=report)
                data_montgomery.append(xray)
        return data_montgomery
