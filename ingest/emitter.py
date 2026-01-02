import json
import logging
from typing import Dict

logger = logging.getLogger(__name__)

def emit_to_stdout(payload: Dict):
    logger.info("EMIT_PAYLOAD_START")
    print(json.dumps(payload, indent=2))
    logger.info("EMIT_PAYLOAD_END")
