
'''
This is the first program I wrote
1.Just testing out some stuff and getting  a feel of the json file
2. Getting a feel of the fhir.resources library
3. working out how to extract elements from each resource
4. Tested it on the Patient and Condition resource for now

'''

from fhir.resources.condition import Condition
from fhir.resources.patient import Patient

import pandas as pd
import json

from pathlib import Path

# Load FHIR data (assuming it's stored in a JSON file)
file_path = Path(r'C:\Emis\rhir.json')

with open(file_path, 'r') as f:
    fhir_data = json.load(f)


# Parsing the Patient and Condition Resource
# Testing out tExtracting Elements from these Resources

for resourcelist in fhir_data['entry']:
    if resourcelist['resource']['resourceType'] == "Patient":
        patient_resource = Patient.parse_obj(resourcelist['resource'])
        print("Patient name:",patient_resource.name)
        print("family name:", patient_resource.name[0].family)
        print("Gender is:", patient_resource.gender)
        print("Telecom: ", patient_resource.telecom[0].value)
        print()

    if resourcelist['resource']['resourceType'] == "Condition":
        condition_resource = Condition.parse_obj(resourcelist['resource'])
        print("codedescription :", condition_resource.code.text)




def fhir_patient_to_dataframe(fhir_patients):
    # Extract relevant fields from FHIR Patient resources
    data_Patient = []
    patient_id=""
    name=""
    gender =""
    birth_date=""
    for (patient_details,value) in fhir_patients:
        if patient_details == 'id':
            patient_id=value
            print(patient_id)
        if patient_details == 'gender':
            gender =value
            print("Gender is",value)
        if patient_details == 'birthDate':
            birth_date =value
            print("birth_date is",value)
        if patient_details == 'name':
            name =value[0].family
            print("birth_date is",value)
        # Add more fields as needed
        # Append patient data to list
    data_Patient.append({'PatientID': patient_id, 'Name': name, 'Gender': gender, 'BirthDate': birth_date})

    # Convert list of patient data to DataFrame
    df = pd.DataFrame(data_Patient)
    return df


df_Patient = fhir_patient_to_dataframe(patient_resource)

print(df_Patient)



