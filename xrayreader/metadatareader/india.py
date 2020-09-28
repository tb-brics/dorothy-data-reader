
"""
Class for reading metadata from files of the 
India Dataset
"""

from .reader import Reader


class IndiaMetadaDataReader(Reader):
    """
    India data set does not have any report
    """
    def parse_files(self):
        """
        No data report found
        """
        return []
