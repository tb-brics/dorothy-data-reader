"""
Class for retriving data from several datasets
"""
import importlib
import os.path

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
