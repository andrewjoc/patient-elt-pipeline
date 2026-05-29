import dlt
from synthea_source import synthea

def main():
    pipeline = dlt.pipeline(
        pipeline_name = "patient_elt_pipeline",
        dataset_name="raw",
        destination = "postgres"
    )

    info = pipeline.run(synthea, write_disposition="merge")

    print(info)


if __name__ == "__main__":
    main()