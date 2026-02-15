import typing as T


class TimestampCopyProtocol(T.Protocol):  # pylint: disable=too-few-public-methods
    def CopyFrom(self, other: T.Any) -> None: ...  # pylint: disable=invalid-name


class LogMessagePbProtocol(T.Protocol):  # pylint: disable=too-few-public-methods
    message: str
    utime: TimestampCopyProtocol
