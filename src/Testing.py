

import json
import pathlib
#from resource_utility import create_resource_list
from dataframe_converters import *
import os

from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

#access the environment variables

fhir_file_path = os.getenv('FHIR_FILE_PATH')

with open(fhir_file_path, 'r') as file:
    fhir_data = json.load(file)

resType = []
for rType in fhir_data['entry']:
    resType.append(rType['resource']['resourceType'])
    if rType['resource']['resourceType'] == 'Patient':
        print("Hurray")


#file_path = "..\\data\\input\\rhir.json"

#with open (file_path,'r') as file:
#data = json.load(file)

# Get the current working directory
#current_directory = os.getcwd()

# Define the folder name for the csv files
#folder_name = 'CSVFolder'

# Create the folder if it doesn't exist
#folder_path = os.path.join(current_directory, folder_name)
#if not os.path.exists(folder_path):
    #os.makedirs(folder_path)

#datainputdirectory = "..\\data\\output"
#folder_path = os.path.join(datainputdirectory, folder_name)
#if not os.path.exists(folder_path):
    #os.makedirs(folder_path)