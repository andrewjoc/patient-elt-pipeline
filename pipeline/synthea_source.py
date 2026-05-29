import dlt
import pandas as pd
from pathlib import Path
from schema import Patient, Condition, Immunization, Medication, Procedure
import os


# mapping of csv name to primary key and schema
SOURCE_CONFIG = {
    "patients.csv": {
        "primary_key": "id",
        "schema": Patient
    },
    "conditions.csv": {
        "primary_key": ("encounter", "code"),
        "schema": Condition
    },
    "immunizations.csv": {
        "primary_key": ("encounter", "code"),
        "schema": Immunization
    },
    "medications.csv": {
        "primary_key": ("encounter", "code"),
        "schema": Medication
    },
    "procedures.csv": {
        "primary_key": ("encounter", "code"),
        "schema": Procedure
    }
}


def has_schema(file_name):
    return file_name in SOURCE_CONFIG

def get_schema(file_name):
    return SOURCE_CONFIG[file_name]["schema"]

def get_primary_key(file_name):
    return SOURCE_CONFIG[file_name]["primary_key"]

def load_csv(file_path):
    df = pd.read_csv(file_path)
    records = df.to_dict(orient="records")

    for record in records:
        yield record

@dlt.source
def synthea():
    bucket_url = dlt.config["sources.filesystem.bucket_url"]
    directory_files = os.listdir(str(Path(bucket_url)))
    detected_csv_files= [f for f in directory_files if f.endswith(".csv")]

    for file_name in detected_csv_files:
        csv_path = str(Path(dlt.config["sources.filesystem.bucket_url"]) / Path(file_name))

        # name without file extension (.csv)
        file_prefix = file_name.replace(".csv", "") 

        if has_schema(file_name):
            yield dlt.resource(load_csv(csv_path),
                               name=file_prefix, 
                               columns=get_schema(file_name),
                               primary_key=get_primary_key(file_name),
                               schema_contract="evolve")
        else:
            yield dlt.resource(load_csv(csv_path),
                               name=file_prefix)