# patient-elt-pipeline
End-to-end data pipeline with Streamlit dashboard.

_Disclaimer_: All patient data are synthetically generated using [Synthea](https://synthetichealth.github.io/synthea/#about-landing) for the purposes of development. The data are realistic but do not represent real individuals. The data do not contain Personally Identifiable Information (PII) or Protected Health Information (PHI).


# Setup
Requires [uv](https://docs.astral.sh/uv/getting-started/installation/) and [Docker](https://docs.docker.com/engine/install/)

```
# clone repository
git clone https://github.com/andrewjoc/patient-elt-pipeline.git

# download dependencies
uv sync

# start up the postgres and pgadmin container
docker compose -f ./db/compose.yml up -d

# run the pipeline
uv run pipeline/run.py
```

<br>

Before running the pipeline, `config.toml` and `secrets.toml` must be configured.  
For non-sensitive configuration values, store them in `config.toml`.
```
# config.toml

[destination.filesystem]
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

<br>

After running the pipeline, you can visit the following links to view pgadmin and the analytical dashboard.

| | |
| --- | --- | 
| pgAdmin | localhost |
| Dashboard | localhost |

<br>

To stop the container and remove all data from the named volume 
```
docker compose -f ./db/compose.yml down -v
```



# Citations
- Jason Walonoski, Mark Kramer, Joseph Nichols, Andre Quina, Chris Moesel, Dylan Hall, Carlton Duffett, Kudakwashe Dube, Thomas Gallagher, Scott McLachlan, Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record, Journal of the American Medical Informatics Association, Volume 25, Issue 3, March 2018, Pages 230–238, https://doi.org/10.1093/jamia/ocx079
- https://dlthub.com/docs/pipelines/filesystem/load-data-with-python-from-filesystem-to-filesystem
