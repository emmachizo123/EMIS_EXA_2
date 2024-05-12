
'''
This file contains
'''

from fhir.resources.claim import Claim
from fhir.resources.condition import Condition
from fhir.resources.diagnosticreport import DiagnosticReport
from fhir.resources.observation import Observation
from fhir.resources.patient import Patient
from fhir.resources.procedure import Procedure


def create_resource_list(list_of_resource, resource_dict):
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
        field_dict = {}
        if res['resource']['resourceType'] == 'Patient':
            filter_field(Patient, res['resource'], field_dict)
            resource_dict['Patient'].append(Patient(**field_dict))
        elif res['resource']['resourceType'] == 'Condition':
            filter_field(Condition, res['resource'], field_dict)
            resource_dict['Condition'].append(Condition(**field_dict))
        elif res['resource']['resourceType'] == 'DiagnosticReport':
            filter_field(DiagnosticReport, res['resource'], field_dict)
            resource_dict['DiagnosticReport'].append(DiagnosticReport(**field_dict))
        elif res['resource']['resourceType'] == 'Observation':
            filter_field(Observation, res['resource'], field_dict)
            resource_dict['Observation'].append(Observation(**field_dict))
        elif res['resource']['resourceType'] == 'Procedure':
            filter_field(Procedure, res['resource'], field_dict)
            resource_dict['Procedure'].append(Procedure(**field_dict))
        elif res['resource']['resourceType'] == 'Claim':
            filter_field(Claim, res['resource'], field_dict)
            resource_dict['Claim'].append(Claim(**field_dict))

def filter_field(model, entry, field_dict):
    for key in entry.keys():
        if key in model.elements_sequence():
            field_dict[key] = entry[key]