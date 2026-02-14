import logging
import typing as T

from google.protobuf.timestamp_pb2 import Timestamp
from ry_pg_utils.dynamic_table import DynamicTableDb
from ryutils import log

from .types import LogMessagePbProtocol

LOGGING_CALLBACK_DB = "LogErrorMessages"


def logging_error_db_callback(
    message: str,
    log_message_cls: type[LogMessagePbProtocol],
    db_name: T.Optional[str] = None,
) -> None:
    message_pb = log_message_cls()

    try:
        message_pb.message = message
    except Exception as exc:  # pylint: disable=broad-except
        err_message = f"Failed to log message to DB: {exc}"
        print(err_message)
        message_pb.message = err_message

    if not db_name:
        return

    timestamp = Timestamp()
    timestamp.GetCurrentTime()
    message_pb.utime.CopyFrom(timestamp)
    DynamicTableDb.log_data_to_db(message_pb, db_name, LOGGING_CALLBACK_DB, log_print_failure=False)


def setup_logging(
    log_dir: str,
    log_level: str,
    log_name: str,
    log_message_cls: type[LogMessagePbProtocol],
    downsample_count: int = 1,
) -> None:
    callback = lambda msg, db_name=None: logging_error_db_callback(msg, log_message_cls, db_name)
    log.setup(
        log_dir,
        log_level,
        log_name,
        use_multihandler=False,
        downsample_count=downsample_count,
        callback=callback,
        callback_level=logging.ERROR,
    )
