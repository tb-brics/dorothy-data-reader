"""
Class for retriving data from several datasets
"""
import importlib
import os.path

from .metadatareader.xray_image_metadata import XRayImageMetadata


class DatasetBase:
    """
    """
    dataset =  None
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


class ChinaDataset(DatasetBase):
    dataset = 'china'
    metadata_folder = 'ClinicalReadings'
    images_folder = 'CXR_png'


class MontgomeryDataset(DatasetBase):
    dataset = 'montgomery'
    metadata_folder = 'ClinicalReadings'
    images_folder = 'CXR_png'


class IndiaDataset:
    dataset = 'india'
 
    def __init__(self, **kwargs):
        self.path = kwargs.get("path")
        self.images_folder = kwargs.get("folder", "DatasetA")

    @staticmethod
    def get_metadata(filename):
        return XRayImageMetadata(
                filename=filename,
                has_tb = filename.imagename[0] == 'p'
        )

    def get_image_reader_module(self):
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


class Dataset:
    _datasets = {
        "india": IndiaDataset,
        "montgomery": MontgomeryDataset,
        "china": ChinaDataset
    }

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def _get_dataset(self):
        if self.name not in self._datasets:
            raise ValueError("Dataset not found")
        return self._datasets.get(self.name)(path=self.path)

    def get_data(self):
        dataset = self._get_dataset()
        return dataset.get_data()
