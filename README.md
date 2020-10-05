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
pip install -e https://github.com/tb-brics/dorothy-data-reader
~~~~ 
Doing that, you will have all the needs to start using 
the library
****
## Running the library 
First of all, if you want to get information about the images and
clinical readings, you need to import the 'Dataset' corresponding
to the country you want the information from(China, Montgomery, India).
~~~~
from xrayraeder.data import Dataset
~~~~
To get information from a specific dataset, you will need to use the path where the images are stored.
This will show the name of the dataset which you are getting information from, also 
the name of the images an of the clinical readings.
~~~~
data = Dataset(name = 'name of the contry you want', path = 'path whwere the information is stored')
data.get_data()
~~~~
If you want to see if the patient has tb or not, and the report, you can print it.
It will return tha gender, the age, if the patient has not tb(shows False) or
if he has any abnormality(shows True) and, at the end, the report.

~~~~
print(data.getdata()['data']['metadata'][0])
~~~~
 


