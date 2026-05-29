CREATE DATABASE patient_elt_pipeline;

CREATE USER loader WITH PASSWORD '<password>';

ALTER DATABASE patient_elt_pipeline OWNER TO loader;