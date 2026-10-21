import logging

logger = logging.getLogger(__name__)


def run_export(rows, sink):
    logger.info("Starting export")
    for row in rows:
        logger.info("exporting row %s", row)
        sink.write(row)
    logger.info("Export finished rows=%d", len(rows))


def validate_partitions(partitions: list, required: list) -> bool:
    """Validate required partitions are present."""
    for p in required:
        if p not in partitions:
            logger.error("partition %s not found, skipping export", p)
            return False
    return True
