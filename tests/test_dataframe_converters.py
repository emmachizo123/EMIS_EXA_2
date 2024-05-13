import pytest
from test_data.resourcetypes import *
import sys
sys.path.append('..')
from src.dataframe_converters import *

## Basic test to check the return type of the functions
## and check that the exception raised when an empty list
## is passed works

def test_fhir_patient_to_dataframe_type()-> None:
    assert isinstance(fhir_patient_to_dataframe(patient),pd.DataFrame)
    with pytest.raises(ValueError, match="List must be non-empty"):
        fhir_patient_to_dataframe([])

def test_fhir_condition_to_dataframe()-> None:
    assert isinstance(fhir_condition_to_dataframe(condition),pd.DataFrame)
    with pytest.raises(ValueError, match="List must be non-empty"):
        fhir_condition_to_dataframe([])

def test_fhir_diagnosticReport_to_dataframe()-> None:
    assert isinstance(fhir_diagnosticReport_to_dataframe(diagnosticReport),pd.DataFrame)
    with pytest.raises(ValueError, match="List must be non-empty"):
        fhir_diagnosticReport_to_dataframe([])

def test_fhir_observation_to_dataframe()-> None:
    assert isinstance(fhir_observation_to_dataframe(observation),pd.DataFrame)
    with pytest.raises(ValueError, match="List must be non-empty"):
        fhir_observation_to_dataframe([])

def test_fhir_procedure_to_dataframe()-> None:
    assert isinstance(fhir_procedure_to_dataframe(procedure),pd.DataFrame)
    with pytest.raises(ValueError, match="List must be non-empty"):
        fhir_procedure_to_dataframe([])

def test_fhir_claim_to_dataframe()-> None:
    assert isinstance(fhir_claim_to_dataframe(claim),pd.DataFrame)
    with pytest.raises(ValueError, match="List must be non-empty"):
        fhir_claim_to_dataframe([])
