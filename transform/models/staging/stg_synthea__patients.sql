select
    patients.Id as patient_id,
    patients.GENDER as gender,
    patients.CITY as city,
    patients.STATE as state,
    patients.COUNTY as county,
    patients.HEALTHCARE_EXPENSES as healthcare_expenses,
    patients.HEALTHCARE_COVERAGE as healthcare_coverage,
    patients.INCOME as income
from {{ source('raw_data', 'patients') }}
order by patient_id asc