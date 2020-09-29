"""
Class for retriving data from several datasets
"""
import importlib
import os.path
from .metadatareader.xray_image_metadata import XRayImageMetadata


class DatasetBaseInterface: #pylint: disable=too-few-public-methods
    """
    Interface for Dataset Reader Classes
    """
    dataset = None

    def get_data(self):
        """
        Get images and metadata from a dataset
        """
        raise NotImplementedError



class DatasetBase(DatasetBaseInterface): #pylint: disable=too-few-public-methods
    """
     stores the path where the files are saved
      so that the data can be read.
    """
    dataset = None
    metadata_folder = None
    images_folder = None

    def __init__(self, **kwargs):
        self.path = kwargs.get("path")
        self.metadata_path = os.path.join(self.path,
                                          self.metadata_folder)
        self.images_path = os.path.join(self.path,
                                        self.images_folder)

    def get_data(self):
        metadata_reader = importlib.import_module(
                f"xrayreader.metadatareader.{self.dataset}").Reader
        images_reader = importlib.import_module(
                f"xrayreader.images.{self.dataset}").Reader

        data = {"data": {}}
        data['data']['dataset'] = self.dataset
        if self.images_folder:
            data['data']['images'] = images_reader(path=self.images_path).get_images()
        if self.metadata_folder:
            data['data']['metadata'] = metadata_reader(path=self.metadata_path).parse_files()
        return data


class ChinaDataset(DatasetBase):#pylint: disable=too-few-public-methods
    """
    Get metadata and images from China.
    """
    dataset = 'china'
    metadata_folder = 'ClinicalReadings'
    images_folder = 'CXR_png'


class MontgomeryDataset(DatasetBase): #pylint: disable=too-few-public-methods
    """
    Get metadata and images from Montgomery.
    """
    dataset = 'montgomery'
    metadata_folder = 'ClinicalReadings'
    images_folder = 'CXR_png'


class IndiaDataset(DatasetBaseInterface):
    """
    Get information from India.
    """
    dataset = 'india'

    def __init__(self, **kwargs):
        self.path = kwargs.get("path")
        self.images_folder = kwargs.get("folder", "DatasetA")

    @staticmethod
    def get_metadata(filename):
        """
        Returns the name of the file
        and tells whether the patient from India has tb.
        """
        return XRayImageMetadata(
                filename=filename,
                has_tb=filename.imagename[0] == 'p'
        )

    def get_image_reader_module(self):
        """
        Returns the path where the images are saved
        and the dataset where this images are from.
        """
        images_reader = importlib.import_module(
                f"xrayreader.images.{self.dataset}").Reader
        return images_reader(path=self.path,
                             dataset=self.images_folder)

    def get_data(self):
        data = {"data": {}}
        data['data']['dataset'] = self.dataset
        if self.images_folder:
            images = self.get_image_reader_module().get_images()
            data['data']['images'] = images
            data['data']['metadata'] = [self.get_metadata(img) for img in images]
        return data


class Dataset: #pylint: disable=too-few-public-methods
    """
    Returns the data from a specific dataset,
    India, China, or Montgomery.
    """
    _datasets = {
        "india": IndiaDataset,
        "montgomery": MontgomeryDataset,
        "china": ChinaDataset
    }

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def _get_dataset(self):
        """
        Returns the name and the path of the dataset.
        """
        if self.name not in self._datasets:
            raise ValueError("Dataset not found")
        return self._datasets.get(self.name)(path=self.path)

    def get_data(self):
        """
        Return the data from the dataset.
        """
        dataset = self._get_dataset()
        return dataset.get_data()
