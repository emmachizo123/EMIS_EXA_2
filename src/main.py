
import json
import sys
sys.path.append('..')
import json
import sys
from pathlib import Path


import pathlib
from utilities.resource_utility import create_resource_list, write_to_csv
from dataframe_converters import *

from dotenv import load_dotenv
import os

def main( )-> None:
    """
    Function processes resource type medical information stored
    in a json file and converts them to dataframes and stores them
    in a csv file

    Returns
    -------
    None

    """

    # load environment variables from .env file
    load_dotenv()

    # access the environment variables for the fhir data file

    fhir_file_path = os.getenv('FHIR_FILE_PATH')

    with open(fhir_file_path, 'r') as file:
        fhir_data = json.load(file)

    resType = []
    for rType in fhir_data['entry']:
        resType.append(rType['resource']['resourceType'])

    resDict = {key: [] for key in set(resType)}
    create_resource_list(fhir_data['entry'], resDict)

    patient_df    = fhir_patient_to_dataframe(resDict['Patient'])
    condition_df  = fhir_condition_to_dataframe(resDict['Condition'])
    diagnostic_df = fhir_diagnosticReport_to_dataframe(resDict['DiagnosticReport'])
    observaton_df = fhir_observation_to_dataframe(resDict['Observation'])
    procedure_df  = fhir_procedure_to_dataframe(resDict['Procedure'])
    claim_df      = fhir_claim_to_dataframe(resDict['Claim'])

    write_to_csv(
        ('patient', patient_df),
        ('condition', condition_df),
        ('diagnostic', diagnostic_df),
        ('observation', observaton_df),
        ('procedure', procedure_df),
        ('claim', claim_df)
    )


if __name__ == '__main__':
    main()
