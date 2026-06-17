# patient-elt-pipeline
End-to-end data pipeline with Streamlit dashboard.

_Disclaimer_: All patient data are synthetically generated using [Synthea](https://synthetichealth.github.io/synthea/#about-landing) for the purposes of development. The data are realistic but do not represent real individuals. The data do not contain Personally Identifiable Information (PII) or Protected Health Information (PHI).

# Tools/Software Used
- Synthea, for synthetic patient generation
- dlt, for data extraction
- dbt, for data transformation
- Docker
- PostgreSQL
- Streamlit, for visualizing cleaned data from PostgreSQL


# Setup
Requires [uv](https://docs.astral.sh/uv/getting-started/installation/) and [Docker](https://docs.docker.com/engine/install/)

```
# clone repository
git clone https://github.com/andrewjoc/patient-elt-pipeline.git

# update uv environment
uv sync

# start up the postgres and pgadmin container
docker compose -f ./postgres_local/compose.yaml up -d

# run the pipeline
uv run pipeline/run.py

# navigate to transform directory and run dbt
cd transform
uv run dbt run

# launch streamlit dashboard
uv run streamlit run dashboard/App.py

# stop the container and remove managed volume
docker compose -f ./postgres_local/compose.yaml down -v
```
<br>

| | Link |
| --- | --- | 
| pgAdmin | [http://localhost:8080](http://localhost:8080) |
| Dashboard | [http://localhost:8501](http://localhost:8501) |

<br>

# Configurations
Before running the pipeline, `config.toml` and `secrets.toml` must be configured.  
For non-sensitive configuration values, store them in `config.toml`.
```
# config.toml

[sources.filesystem]
bucket_url = "bucket_url"

[destination.filesystem]
bucket_url = "bucket_url"
```

For credentials such as API keys and passwords, store them in `secrets.toml`. 
```
# secrets.toml

[sources.filesystem.credentials]
aws_access_key_id = "aws_access_key_id"
aws_secret_access_key = "aws_secret_access_key"

[destination.filesystem.credentials]
aws_access_key_id = "aws_access_key_id"
aws_secret_access_key = "aws_secret_access_key"

[destination.postgres.credentials]
database = "db_name"
username = "postgres_user"
password = "postgres_password"
host = "localhost"
post = 5432
connect_timeout = 15
```


# Citations
- Jason Walonoski, Mark Kramer, Joseph Nichols, Andre Quina, Chris Moesel, Dylan Hall, Carlton Duffett, Kudakwashe Dube, Thomas Gallagher, Scott McLachlan, Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record, Journal of the American Medical Informatics Association, Volume 25, Issue 3, March 2018, Pages 230–238, https://doi.org/10.1093/jamia/ocx079
- https://dlthub.com/docs/pipelines/filesystem/load-data-with-python-from-filesystem-to-filesystem
- https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary
