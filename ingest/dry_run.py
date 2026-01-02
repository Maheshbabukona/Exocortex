import json
import logging
import os
from pipeline import run_ingestion_pipeline

logging.basicConfig(level=logging.INFO)

STATE_FILE = ".dry_run_state.json"


def load_state() -> set:
    if not os.path.exists(STATE_FILE):
        return set()
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return set(json.load(f))


def save_state(hashes: set) -> None:
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(hashes), f, indent=2)


# Load persisted state ONCE per CLI run
SEEN_HASHES = load_state()


def is_already_ingested_stub(file_hash: str) -> bool:
    return file_hash in SEEN_HASHES


def emit_stub(payload: dict) -> None:
    SEEN_HASHES.add(payload["file_hash"])

    print("\n" + "=" * 80)
    print(f"SOURCE: {payload['source_path']}")
    print(f"HASH:   {payload['file_hash']}")
    print(f"PAGES:  {len(payload['pages'])}")


if __name__ == "__main__":
    run_ingestion_pipeline(
        folder_path=r"D:\Exocortex\pdfs",
        is_already_ingested=is_already_ingested_stub,
        emit=emit_stub,
    )

    # Persist state AFTER pipeline completes successfully
    save_state(SEEN_HASHES)
