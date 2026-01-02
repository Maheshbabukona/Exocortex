import argparse
import logging
from pathlib import Path

from ingest.pipeline import run_ingestion_pipeline
from ingest.manifest import is_already_ingested, record_ingestion
from ingest.emitter import emit_to_stdout

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder",type=str, help ="Folder containing PDFs")
    args=parser.parse_args()

    run_ingestion_pipeline(
        folder_path=str(Path(args.folder)),
        is_already_ingested=is_already_ingested,
        emit=lambda payload:(
            emit_to_stdout(payload),
            record_ingestion(payload["file_hash"])
        )
    )

if __name__ == "__main__":
    main()