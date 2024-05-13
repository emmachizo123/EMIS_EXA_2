import pandas as pd
from typing import List

def fhir_patient_to_dataframe(fhir_patients: List) -> pd.DataFrame:
    """
    Function takes a list of Patient resource data and processes it into
    a dataframe

    Parameters
    ----------
    fhir_patients : List
        List of Patient resource data.

    Returns
    -------
    df : pd.DataFrame
        Returns patient data in a dataframe.

    """
    # Extract relevant fields from FHIR Patient resources
    if fhir_patients == []:
        raise ValueError("List must be non-empty")

    data = []
    for patient in fhir_patients:
        patient_id = patient.id
        last_name  = patient.name[0].family
        first_name = patient.name[0].given[0]
        gender     = patient.gender
        birth_date = patient.birthDate.isoformat() if patient.birthDate else None
        # Add more fields as needed

        # Append patient data to list
        data.append({'PatientID': patient_id, 'FirstName': first_name, 'LastName': last_name,
                     'Gender': gender, 'BirthDate': birth_date})

    # Convert list of patient data to DataFrame
    df = pd.DataFrame(data)
    return df

def fhir_condition_to_dataframe(fhir_conditions: List) -> pd.DataFrame:
    """
    Function takes a list of Condition resource data and processes it into
    a dataframe

    Parameters
    ----------
    fhir_conditions : List
        List of Condition resource data.

    Returns
    -------
    df : pd.DataFrame
        Returns condition data in a dataframe.

    """
    # Extract relevant fields from FHIR Patient resources
    if fhir_conditions == []:
        raise ValueError("List must be non-empty")

    data = []
    for condition in fhir_conditions:
        ConditionID     = condition.id
        Code            = condition.code.coding[0].code
        codeDescription = condition.code.text
        onsetDatetime   = condition.onsetDateTime.isoformat()
        recordedDate    = condition.recordedDate.isoformat()
        # Add more fields as needed

        # Append patient data to list
        data.append({'ConditionID': ConditionID, 'Code': Code, 'codeDescription': codeDescription,
                     'onsetDatetime': onsetDatetime, 'recordedDate': recordedDate})

    # Convert list of patient data to DataFrame
    df = pd.DataFrame(data)
    return df

def fhir_diagnosticReport_to_dataframe(fhir_diagnosticReports):
    """
    Function takes a list of DiagnosticReport resource data and processes it into
    a dataframe

    Parameters
    ----------
    fhir_diagnosticReports : List
        List of DiagnosticReport resource data.

    Returns
    -------
    df : pd.DataFrame
        Returns diagnosticReport data in a dataframe.

    """
    # Extract relevant fields from FHIR Patient resources
    if fhir_diagnosticReports == []:
        raise ValueError("List must be non-empty")

    data = []
    for diagnosticReport in fhir_diagnosticReports:
        DiagnosticReport_ID  = diagnosticReport.id
        Status               = diagnosticReport.status
        code                 = diagnosticReport.code.coding[0].code
        codeDescription      = diagnosticReport.code.coding[0].display
        effectiveDatetime    = diagnosticReport.effectiveDateTime.isoformat()
        dateIssued           = diagnosticReport.issued.isoformat()
        Performer            = diagnosticReport.performer[0].display
        # Add more fields as needed

        # Append patient data to list
        data.append({'DiagnosticReport_ID': DiagnosticReport_ID, 'DiagnosticReport_ID': DiagnosticReport_ID,
                     'Status': Status, 'Code': code, 'codeDescription': codeDescription,
                     'effectiveDatetime': effectiveDatetime, 'dateIssued': dateIssued,
                     'Performer': Performer})

    # Convert list of patient data to DataFrame
    df = pd.DataFrame(data)
    return df

def fhir_observation_to_dataframe(fhir_observations):
    """
    Function takes a list of Observation resource data and processes it into
    a dataframe

    Parameters
    ----------
    fhir_observations : List
        List of Observation resource data.

    Returns
    -------
    df : pd.DataFrame
        Returns observation data in a dataframe.

    """
    # Extract relevant fields from FHIR Patient resources
    if fhir_observations == []:
        raise ValueError("List must be non-empty")

    data = []
    for observation in fhir_observations:
        Observation_ID  = observation.id
        Status          = observation.status
        Code            = observation.code.coding[0].code
        codeDescription = observation.code.text
        effectiveDatetime    = observation.effectiveDateTime.isoformat()
        dateIssued           = observation.issued.isoformat()
        # Add more fields as needed

        # Append patient data to list
        data.append({'Observation_ID': Observation_ID, 'Status': Status, 'Code': Code,
                     'codeDescription': codeDescription,
                     'effectiveDatetime': effectiveDatetime, 'dateIssued': dateIssued})

    # Convert list of patient data to DataFrame
    df = pd.DataFrame(data)
    return df

def fhir_procedure_to_dataframe(fhir_procedures: List) -> pd.DataFrame:
    """
    Function takes a list of Procedure resource data and processes it into
    a dataframe

    Parameters
    ----------
    fhir_procedures : List
        List of Procedure resource data.

    Returns
    -------
    df : pd.DataFrame
        Returns Procedure data in a dataframe.

    """
    # Extract relevant fields from FHIR Patient resources
    if fhir_procedures == []:
        raise ValueError("List must be non-empty")

    data = []
    for procedure in fhir_procedures:
        Procedure_ID    = procedure.id
        Status          = procedure.status
        Code            = procedure.code.coding[0].code
        codeDescription = procedure.code.text
        Location        = procedure.location.display
        # Add more fields as needed

        # Append patient data to list
        data.append({'Procedure_ID': Procedure_ID, 'Status': Status, 'Code': Code,
                     'codeDescription': codeDescription, 'Location': Location})

    # Convert list of patient data to DataFrame
    df = pd.DataFrame(data)
    return df

def fhir_claim_to_dataframe(fhir_claims: List) -> pd.DataFrame:
    """
    Function takes a list of Claims resource data and processes it into
    a dataframe

    Parameters
    ----------
    fhir_claims : List
        List of Claims resource data.

    Returns
    -------
    df : pd.DataFrame
        Returns claims data in a dataframe.

    """
    # Extract relevant fields from FHIR Patient resources
    if fhir_claims == []:
        raise ValueError("List must be non-empty")

    data = []
    for claim in fhir_claims:
        Claim_ID          = claim.id
        Status            = claim.status
        typeCode          = claim.type.coding[0].code
        Use               = claim.use
        Patient           = claim.patient.display
        BillableStartDate = claim.billablePeriod.start.isoformat()
        BillableEndDate   = claim.billablePeriod.end.isoformat()
        DateCreated       = claim.created.isoformat()
        PriorityCode      = claim.priority.coding[0].code
        InsuranceCoverage = claim.insurance[0].coverage.display
        Total             = claim.total.currency + " {:,.2f}".format(claim.total.value)

        # Add more fields as needed

        # Append patient data to list
        data.append({'Claim_ID': Claim_ID, 'Status': Status, 'typeCode': typeCode, 'Patient': Patient,
                     'BillableStartDate': BillableStartDate, 'BillableEndDate': BillableEndDate,
                     'DateCreated': DateCreated, 'PriorityCode': PriorityCode, 'InsuranceCoverage': InsuranceCoverage,
                     'Total': Total})

    # Convert list of patient data to DataFrame
    df = pd.DataFrame(data)
    return df
