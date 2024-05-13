


README
 
Application Name :
EXA_FHIR App

Brief Summary
FHIR ( Fast Healthcare Interoperability Resources) is the standard for exchanging 
healthcare information and even though the  goal of FHIR is to facilitate interoperability
between different healthcare systems and applications by providing a standardized way 
to exchange healthcare data, Our analytics teams find this format difficult to work
with when creating dashboards and visualizations.
The EXA_FHIR transformation pipeline application is therefore  a scalable ETL  
data pipeline that consumes FHIR messages and transforms them into a 
tabular format for easier and further data analysis and  business intelligence.
In summary , the  application extracts fhir data , transforms it into a tabular 
format(in this version CSV format)  and loads it into a designation .
 
 
Table of Contents
 
1.  Work  flow
2. Features
3.  Description of Modules
4.  Installation
5.  Usage
6.  Next Steps
 
 

Workflow

FHIR DATA------->EXTRACT-------->TRANSFORM--------->LOAD
The EXA_FHIR sofware reads FHIR( Fast Healthcare Interoperability Resources) data and transforms it
into CVS format. A successful thorouput will result to the cleansing and the outputing of fhir data
as CSV files in /data/output/CSVFolder

1. Features
- Feature 1: Extraction (Reading FHIR data )
The Extraction Module loads the FHIR file from a file location. The path to the file location is stored in the project .env file  for flexibility purposes.
 
- Feature 2 : Transformation
The application navigates through the  nesting of the json file , storing each resource type and it’s elements into a dictionary which it then transforms into a pandas data frame.
In order to do this , the data is cleansed.
Part of cleansing involves removing the  wrong fields that don’t belong to a Resource using a filter function that I wrote.
Using other  more rigorous processes , the fhir data is transformed into a pandas dataframe .

- The Transformation Modules
resource_utility.py: The main data transformation module.
create_resource_list: This function takes entry from a bundle , initializes the data to the 
right resource and groups the different resource data into the resource dictionary .
Mutates the resource_dict in place
_filter_field: function filters off attributes that do not belong to the resource type , and stores the right attributes and its values in the dictionary — field_dict
write_to_csv:  The function writes a  pandas DataFrame to a csv file
 
- Feature 3: Loading the dataframe to CSV
The loading module takes the pandas dataframe representing each 
FHIR Resource and writes them to a file as CSV.


The Loading Modules
main.py
 
Feature  4: Testing the application
The Testing module uses Python’s  pytest to  do unit and integration test making sure that the application classes are working together and functions are returning the right data .
The Testing Modules:
test_dataframe_converters.py
run_tests.py
resourcetypes.py

2. Description of Modules

main.py:
--Entry point into the application
--Calls the utility classes

dataframe_converters.py
--Contains functions that take a list of  each FHIR resource and processes it into a dataframe
resource_utility.py
--Contains  -filter_field() function that filters off attributes that do not belong to the resource type and stores the right attributes and its values in the dictionary
run_tests.py
--Initiates the test and loads pytest
---Imports subprocess


resourcetypes.py
--Holds the test data

test_dataframe_converters.py
--Contains the actual test functions
--Basic test to check return types of functions
--Test of exception is raised for an empty list
 
.env
--Contains some environmental variables for file paths
Requirements.txt
--Contains all the dependencies
 
 
 
 3. Installation
To install the project simply clone the repository and install the dependencies using 
the following steps:

1. 	git clone https://github.com/emmachizo123/EMIS_EXA_2
2. 	cd EMIS_EXA_2
3. 	pip install -r requirements.txt
4. 	 create .env file if it did not come with the cloned repository.
The project requires a .env file.
Because the .env file for this project doesn’t have any sensitive information, 
I have gone against the rules by adding it to the repository (often seen as a bad idea) 
just to be sure users have it and the code doesn’t break.
If the .env file isn’t part of the application, then it  needs to be created.
In that case create a .env file in the project root and copy the following into it:
 
# .env file
FHIR_FILE_PATH = ../data/input/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json
CSV_FOLDER_NAME =CSVFolder
DATAOUTPUT_DIRECTORY = ../data/output
 
 
Usage
To run the application:
Use the following steps:
Open a command line prompt
Change directory to EMIS_EXA_2 folder
From this directory run:
python main.py
 
 
 
To Test the Application
To run the unit and integration test use the following steps :
From a command line navigate to EMIS_EXA_2 and  run:
python run_tests.py
 
 
 
Next Steps
Because of the limited time there are several ideas that I didn’t explore and implement.
1. 	OOP design  and development
I would  love to have built this application using a full-on OOP design and development. 
It would have brought the beauty and benefits of OOP such a reusability , 
flexibility , portability , security etc .
 
2. 	More Data Exploration
Even though there are about 17 Resource Types in the data file we I used for development,
I was only able to explore just six types (Patient, Condition, Observation , DiagnosticReport,
Claim, Procedure ).
Giving more time I would explore the other resource types.
 
3. 	 Robust Testing
I didn’t write exhaustive test script like I would normally do. 
This will be one area to make improvements

4. 	Containerization with Docker
I ran into some WSL(windows subsystem for Linux) issues that crashed my Docker Desktop and 
there for  made it impossible to containerize the application. 
This would be a very important addition that I will make on the application 
if I had more time
 
 
 
