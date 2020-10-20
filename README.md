# Dorothy Data Reader 
****
Library that reads the data obtained by
analysing x-ray images and reports of the patients.
****
## Requirements 
To start using the library, you must download
the clinical readings and the images that you want to 
analyse, and save them in your computer(you will
need the path of them to run the code).
After that, you need to install the repository
~~~~
pip install git+https://github.com/tb-brics/dorothy-data-reader.git
~~~~ 
Doing that, you will have all the needs to start using 
the library
****
## Running the library 
First of all, if you want to get information about the images and
clinical readings, you need to import the 'Dataset' corresponding
to the country you want the information from(China, Montgomery, India).
~~~~
from xrayreader import Dataset
~~~~
To get information from a specific dataset, you will need to use the path where the images are stored.
This will show the name of the dataset which you are getting information from, also 
the name of the images and of the clinical readings.
~~~~
data = Dataset(name = 'name of the country you want', path = 'path where the information is stored')
data.get_data()
~~~~
If you want to see if the patient has tb or not, and the report, you can print it.
It will return tha gender, the age, if the patient has not tb(shows False) or
if he has any abnormality(shows True) and, at the end, the report.

~~~~
print(data.getdata()['data']['metadata'][0])
~~~~
It will return something like:
~~~~
<the path where the image is stored>: the gender[string]-age[(int) 'years']
-Boolean(True-has tb or False-don't have tb)-report[string]
~~~~
****
## Extending the Library
****
To add new databases in the library, the first step is:
create a python file inside of metadatareader for the desired country data.
~~~~
china.py
~~~~
This file must have a 'Reader' class, which will inherit the functions and methods of
'ReaderBase' (get_filenames and parse_files - the last one is responsible to store
the patient data -age, gender and report) and will be able to get the data from the clinical
readings and return them into a list.
~~~~
class Reader(ReaderBase):
~~~~
Inside of the Reader, functions must be established to handle the specifics of the 
data you want to insert.
****
The next step is to create another python file, now inside of 'images'.
~~~~
china.py
~~~~
This file must have a 'Reader' class, that inherits the methods and functions
set out in 'ReaderBase' (like 'get_filenames' and 'get_data'), just like before. 
Using this, it will be able to get the filenames of the images and return them.

****
After that, it is necessary to create a class inside of data.py, which
will inherit the functions and methods of DatasetBase and through DatasetBaseInterface
recognize the path used and return the desired data and information from
clinical readings and images.
If the data does not have reports and the information about whether or not the patient
has tb is in the filename of the image, this should be resolved in this dataset.
~~~~
class ChinaDataset(DatasetBase):
~~~~
 


