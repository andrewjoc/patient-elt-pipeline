from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class Patient(BaseModel):
    Id: str
    BIRTHDATE: date
    DEATHDATE: Optional[date]
    SSN: Optional[str]
    DRIVERS: Optional[str]
    PASSPORT: Optional[str]
    PREFIX: Optional[str]
    FIRST: Optional[str]
    MIDDLE: Optional[str]
    LAST: Optional[str]
    SUFFIX: Optional[str]
    MAIDEN: Optional[str]
    MARITAL: Optional[str]
    RACE: Optional[str]
    ETHNICITY: Optional[str]
    GENDER: Optional[str]
    BIRTHPLACE: Optional[str]
    ADDRESS: Optional[str]
    CITY: Optional[str]
    STATE: Optional[str]
    COUNTY: Optional[str]
    FIPS: Optional[str]
    ZIP: Optional[str]
    LAT: Optional[float]
    LON: Optional[float]
    HEALTHCARE_EXPENSES: Optional[float]
    HEALTHCARE_COVERAGE: Optional[float]
    INCOME: Optional[float]

class Condition(BaseModel):
    START: Optional[date]
    STOP: Optional[date]
    PATIENT: Optional[str]
    ENCOUNTER: str
    SYSTEM: Optional[str]
    CODE: str
    DESCRIPTION: Optional[str]

class Immunization(BaseModel):
    DATE: Optional[datetime]
    PATIENT: Optional[str]
    ENCOUNTER: str
    CODE: str
    DESCRIPTION: Optional[str]
    BASE_COST: Optional[float]

class Medication(BaseModel):
    START: Optional[datetime]
    STOP: Optional[datetime]
    PATIENT: Optional[str]
    PAYER: Optional[str]
    ENCOUNTER: str
    CODE: str
    DESCRIPTION: Optional[str]
    BASE_COST: Optional[float]
    PAYER_COVERAGE: Optional[float]
    DISPENSES: Optional[int]
    TOTALCOST: Optional[float]
    REASONCODE: Optional[str]
    REASONDESCRIPTION: Optional[str]

class Procedure(BaseModel):
    START: Optional[datetime]
    STOP: Optional[datetime]
    PATIENT: Optional[str]
    ENCOUNTER: Optional[str]
    SYSTEM: Optional[str]
    CODE: Optional[str]
    DESCRIPTION: Optional[str]
    BASE_COST: Optional[float]
    REASONCODE: Optional[str]
    REASONDESCRIPTION: Optional[str]