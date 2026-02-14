import typing as T


class TimestampCopyProtocol(T.Protocol):
    def CopyFrom(self, other: T.Any) -> None: ...


class LogMessagePbProtocol(T.Protocol):
    message: str
    utime: TimestampCopyProtocol
