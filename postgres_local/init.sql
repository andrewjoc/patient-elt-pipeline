CREATE DATABASE patient_elt_pipeline;

CREATE USER loader WITH PASSWORD 'loader_password';

ALTER DATABASE patient_elt_pipeline OWNER TO loader;