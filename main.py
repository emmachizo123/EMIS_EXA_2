import json
import pathlib
from resource_utility import create_resource_list
from dataframe_converters import *

def main() -> None:
    """
        Function processes resource type medical information stored
        in a json file and converts them to dataframes

        Returns
        -------
        None

    """
    """Initially had the json file in my drive. I copied it over to the project directory"""
    #file_path = pathlib.Path(r'C:\Emis\rhir.json')

    #with open(file_path, 'r') as f:
        #fhir_data = json.load(f)

    with open("rhir.json", 'r') as f:
        fhir_data = json.load(f)

    resType = []
    for rType in fhir_data['entry']:
        resType.append(rType['resource']['resourceType'])

    resDict = {key: [] for key in set(resType)}

    create_resource_list(fhir_data['entry'], resDict)

    patient_df = fhir_patient_to_dataframe(resDict['Patient'])
    print("******Patient Data Frame*****")
    print(patient_df.head())
    print()

    condition_df = fhir_condition_to_dataframe(resDict['Condition'])
    print("****** Condition Data Frame*****")
    print(condition_df.head())
    print()

    diagnostic_df = fhir_diagnosticReport_to_dataframe(resDict['DiagnosticReport'])
    print("****** DiagnosticReport DataFrame*****")
    print(diagnostic_df.head())
    print()

    observaton_df = fhir_observation_to_dataframe(resDict['Observation'])
    print("****** Observation DataFrame*****")
    print(observaton_df.head())
    print()

    procedure_df = fhir_procedure_to_dataframe(resDict['Procedure'])
    print("****** Procedure DataFrame*****")
    print(procedure_df.head())
    print()

    claim_df = fhir_claim_to_dataframe(resDict['Claim'])
    print("****** Claim DataFrame*****")
    print(claim_df.head())


if __name__ == '__main__':
    main()

import json
import pathlib
from resource_utility import create_resource_list, write_to_csv
from dataframe_converters import *


def main() -> None:
    """
    Function processes resource type medical information stored
    in a json file and converts them to dataframes and stores them
    in a csv file

    Returns
    -------
    None

    """

    """Initially had the json file in my drive. I copied it over to the project directory"""
    # file_path = pathlib.Path(r'C:\Emis\rhir.json')

    # with open(file_path, 'r') as f:
    # fhir_data = json.load(f)

    with open("rhir.json", 'r') as f:
        fhir_data = json.load(f)

    resType = []
    for rType in fhir_data['entry']:
        resType.append(rType['resource']['resourceType'])

    resDict = {key: [] for key in set(resType)}
    create_resource_list(fhir_data['entry'], resDict)

    patient_df = fhir_patient_to_dataframe(resDict['Patient'])
    condition_df = fhir_condition_to_dataframe(resDict['Condition'])
    diagnostic_df = fhir_diagnosticReport_to_dataframe(resDict['DiagnosticReport'])
    observaton_df = fhir_observation_to_dataframe(resDict['Observation'])
    procedure_df = fhir_procedure_to_dataframe(resDict['Procedure'])
    claim_df = fhir_claim_to_dataframe(resDict['Claim'])

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