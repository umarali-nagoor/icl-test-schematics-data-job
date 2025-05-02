import logging

logger = logging.getLogger(__name__)


def run_export(rows, sink):
    logger.info("Starting export")
    for row in rows:
        logger.info("exporting row %s", row)
        sink.write(row)
    logger.info("Export finished rows=%d", len(rows))
