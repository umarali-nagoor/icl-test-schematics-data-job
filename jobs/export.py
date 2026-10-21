import logging

logger = logging.getLogger(__name__)


def run_export(rows, sink):
    logger.info("Starting export")
    for row in rows:
        logger.info("exporting row %s", row)
        sink.write(row)
    logger.info("Export finished rows=%d", len(rows))


def export_with_audit(rows: list, sink) -> int:
    """Export rows with per-row audit trail."""
    written = 0
    for row in rows:
        logger.info("exporting row: %s", row)
        sink.write(row)
        logger.info("row written: %s", row)
        written += 1
    return written
