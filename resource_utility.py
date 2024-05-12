import os

from fhir.resources.claim import Claim
from fhir.resources.condition import Condition
from fhir.resources.diagnosticreport import DiagnosticReport
from fhir.resources.observation import Observation
from fhir.resources.patient import Patient
from fhir.resources.procedure import Procedure
from fhir.resources import FHIRAbstractModel
from typing import List, Type


def create_resource_list(list_of_resource: List, resource_dict: dict) -> None:
    """
    The function takes the entry from a bundle, initializes the data to the right
    resource and groups the different resource data into the resource dictionary.
    Mutates the resource_dict inplace

    Parameters
    ----------
    list_of_resource : List
        This is the entry from a bundle, and is a list of several resources.
    resource_dict : dict
        (key = name_of_resource, value = list of resource data ). data is processed into the dictionary

    Returns
    -------
    None

    """
    for res in list_of_resource:
        field_dict = {}  # will contain the attributes (and their values) that belong to a resource

        if res['resource']['resourceType'] == 'Patient':
            _filter_field(Patient, res['resource'], field_dict)
            resource_dict['Patient'].append(Patient(**field_dict))
        elif res['resource']['resourceType'] == 'Condition':
            _filter_field(Condition, res['resource'], field_dict)
            resource_dict['Condition'].append(Condition(**field_dict))
        elif res['resource']['resourceType'] == 'DiagnosticReport':
            _filter_field(DiagnosticReport, res['resource'], field_dict)
            resource_dict['DiagnosticReport'].append(DiagnosticReport(**field_dict))
        elif res['resource']['resourceType'] == 'Observation':
            _filter_field(Observation, res['resource'], field_dict)
            resource_dict['Observation'].append(Observation(**field_dict))
        elif res['resource']['resourceType'] == 'Procedure':
            _filter_field(Procedure, res['resource'], field_dict)
            resource_dict['Procedure'].append(Procedure(**field_dict))
        elif res['resource']['resourceType'] == 'Claim':
            _filter_field(Claim, res['resource'], field_dict)
            resource_dict['Claim'].append(Claim(**field_dict))

def _filter_field(model: FHIRAbstractModel, entry: dict, field_dict: dict) -> None:
    """
    Filters off attributes that do not belong to the resource type, and stores
    the right attributes and its values in the dictionary - field_dict

    Parameters
    ----------
    model : FHIRAbstractModel
        The resource type .
    entry : dict
        A single resource data of the passed resource type.
    field_dict : dict
        Dictionary to store the right attributes and its value.

    Returns
    -------
    None

    """
    for key in entry.keys():
        if key in model.elements_sequence():
            field_dict[key] = entry[key]

def write_to_csv(*args, file_path : str = '.' )-> None:
    """


    Parameters
    ----------
    *args : a List of tuple - ( name_of_file, dataframe)

    file_path : str, optional
        Directory path to store the data. The default is '.'.

    Returns
    -------
    None

    """

    # Get the current working directory
    current_directory = os.getcwd()

    #Define the folder name for the csv files
    folder_name ='CSVFolder'

    #Create the folder if it doesn't exist
    folder_path = os.path.join(current_directory,folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


    #for file_name, df in args:
        #df.to_csv(f'{file_path}/{file_name}.csv', index=False)

    for file_name, df in args:
        df.to_csv(f'{folder_path}/{file_name}.csv', index=False)