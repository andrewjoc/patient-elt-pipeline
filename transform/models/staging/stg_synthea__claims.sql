SELECT
    claims.Id as claim_id,
    claims.PATIENTID as patient_id,
    claims.PRIMARYPATIENTINSURANCEID as primary_patient_insurance_id,
    claims.SECONDARYPATIENTINSURANCEID as secondary_patient_insurance_id,
    claims.DIAGNOSIS1 as diagnosis_1,
    claims.DIAGNOSIS2 as diagnosis_2,
    claims.DIAGNOSIS3 as diagnosis_3,
    claims.DIAGNOSIS4 as diagnosis_4,
    claims.DIAGNOSIS5 as diagnosis_5,
    claims.DIAGNOSIS6 as diagnosis_6,
    claims.DIAGNOSIS7 as diagnosis_7,
    claims.DIAGNOSIS8 as diagnosis_8,
    claims.OUTSTANDING1 as outstanding_1,
    claims.OUTSTANDING2 as outstanding_2,
    claims.OUTSTANDINGP as outstanding_p
FROM
    {{ source('raw_data', 'claims') }}