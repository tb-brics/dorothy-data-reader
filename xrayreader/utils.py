"""
Pocketknife functions
"""

import os.path

def parse_filename(filename):
    """
    Parse filename and return its content
    """
    abspath_file = os.path.abspath(filename)
    path, _imagename = os.path.split(abspath_file)
    imagename, extension = os.path.splitext(_imagename)
    if extension[0] == '.':
        extension = extension[1:]
    return path, imagename, extension
