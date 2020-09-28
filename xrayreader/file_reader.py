#!/usr/bin/env python
# coding: utf-8
"""
Module for reading data from XRay Data Set
"""

import glob
import re


files = glob.glob("C:/Users/paola/Desktop/ClinicalReadings/*.txt")


class XRayImageMetadata:
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


class XRayMetadataReader:
    """
    This class stores the filenames into a list.
    """
    def __init__(self, folder):
        self.xrays = []
        self.folder = folder
        self.filenames = None

    def get_filenames(self):
        """
        Return the name of the file in which the report is stored.
        """
        self.filenames = glob.glob(self.folder)
        return self.filenames

    def parse_files(self):
        """
        This function stores patient data(age, gender, report)
        in a list 'data_china'.
        """


class ChinaXRayMetadataReader(XRayMetadataReader):
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
                                         report=report)
                data_china.append(xray)
        return data_china


class MontgomeryXRayMetadataReader(XRayMetadataReader):
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

    def read_files(self):
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
                                         report=report)
                data_montgomery.append(xray)
        return data_montgomery
