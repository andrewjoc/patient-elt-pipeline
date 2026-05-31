import dlt
import pandas as pd
from pathlib import Path
import os
from schema import (
    Claim,
    ClaimTransaction,
    Condition,
    Encounter, 
    Observation,
    Organization,
    Patient,
    Payer,
    Procedure,
    Provider
)


resource_args = {
    "claims.csv": {
        "primary_key": "Id",
        "columns": Claim,
        "schema_contract": "evolve"
    },
    "claims_transactions.csv": {
        "primary_key": "ID",
        "columns": ClaimTransaction,
        "schema_contract": "evolve"
    },
    "conditions.csv": {
        "primary_key": ("encounter", "code"),
        "columns": Condition,
        "schema_contract": "evolve"
    },
    "encounters.csv": {
        "primary_key": "Id",
        "columns": Encounter,
        "schema_contract": "evolve"
    },
    "observations.csv": {
        "primary_key": ("encounter", "code"),
        "columns": Observation,
        "schema_contract": "evolve"
    },
    "organizations.csv": {
        "primary_key": "Id",
        "columns": Organization,
        "schema_contract": "evolve"
    },
    "patients.csv": {
        "primary_key": "id",
        "columns": Patient,
        "schema_contract": "evolve"
    },
    "payers.csv": {
        "primary_key": "Id",
        "columns": Payer,
        "schema_contract": "evolve"
    },
    "procedures.csv": {
        "primary_key": ("encounter", "code"),
        "columns": Procedure,
        "schema_contract": "evolve"
    },
    "providers.csv": {
        "primary_key": "Id",
        "columns": Provider,
        "schema_contract": "evolve"
    }
}

def load_csv(file_path: str):

    df = pd.read_csv(file_path)

    if file_path.endswith("observations.csv"):
        df = df[~df["ENCOUNTER"].isna()]

    records = df.to_dict(orient="records")

    for record in records:
        yield record

@dlt.source
def synthea():
    bucket_url = dlt.config["sources.filesystem.bucket_url"]
    directory_files = os.listdir(str(Path(bucket_url)))
    detected_csv_files= [f for f in directory_files if f.endswith(".csv")]
    print(f"detected csv files: ", detected_csv_files)

    for file_name in detected_csv_files:
        if file_name not in resource_args:
            continue

        csv_path = str(Path(dlt.config["sources.filesystem.bucket_url"]) / Path(file_name))

        # name without file extension (.csv)
        file_prefix = file_name.replace(".csv", "")

        yield dlt.resource(load_csv(csv_path),
                            name=file_prefix,
                            **resource_args[file_name])