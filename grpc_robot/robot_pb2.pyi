from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EmptyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StateResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: str
    def __init__(self, state: _Optional[str] = ...) -> None: ...

class LoadProgramRequest(_message.Message):
    __slots__ = ("nameProgram",)
    NAMEPROGRAM_FIELD_NUMBER: _ClassVar[int]
    nameProgram: str
    def __init__(self, nameProgram: _Optional[str] = ...) -> None: ...

class LoadProgramResponse(_message.Message):
    __slots__ = ("state", "nameProgram")
    STATE_FIELD_NUMBER: _ClassVar[int]
    NAMEPROGRAM_FIELD_NUMBER: _ClassVar[int]
    state: str
    nameProgram: str
    def __init__(self, state: _Optional[str] = ..., nameProgram: _Optional[str] = ...) -> None: ...

class MoveTCPRequest(_message.Message):
    __slots__ = ("pos",)
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: str
    def __init__(self, pos: _Optional[str] = ...) -> None: ...

class IORequest(_message.Message):
    __slots__ = ("pin", "ioState")
    PIN_FIELD_NUMBER: _ClassVar[int]
    IOSTATE_FIELD_NUMBER: _ClassVar[int]
    pin: int
    ioState: bool
    def __init__(self, pin: _Optional[int] = ..., ioState: bool = ...) -> None: ...

class ProgramStateResponse(_message.Message):
    __slots__ = ("state", "programState")
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRAMSTATE_FIELD_NUMBER: _ClassVar[int]
    state: str
    programState: str
    def __init__(self, state: _Optional[str] = ..., programState: _Optional[str] = ...) -> None: ...

class PosResponse(_message.Message):
    __slots__ = ("state", "pos")
    STATE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    state: str
    pos: str
    def __init__(self, state: _Optional[str] = ..., pos: _Optional[str] = ...) -> None: ...

class ToolIdRequest(_message.Message):
    __slots__ = ("toolId",)
    TOOLID_FIELD_NUMBER: _ClassVar[int]
    toolId: int
    def __init__(self, toolId: _Optional[int] = ...) -> None: ...

class ToolIdResponse(_message.Message):
    __slots__ = ("state", "toolId")
    STATE_FIELD_NUMBER: _ClassVar[int]
    TOOLID_FIELD_NUMBER: _ClassVar[int]
    state: str
    toolId: int
    def __init__(self, state: _Optional[str] = ..., toolId: _Optional[int] = ...) -> None: ...

class CoordinateIdRequest(_message.Message):
    __slots__ = ("coordinateId",)
    COORDINATEID_FIELD_NUMBER: _ClassVar[int]
    coordinateId: int
    def __init__(self, coordinateId: _Optional[int] = ...) -> None: ...

class CoordinateIdResponse(_message.Message):
    __slots__ = ("state", "coordinateId")
    STATE_FIELD_NUMBER: _ClassVar[int]
    COORDINATEID_FIELD_NUMBER: _ClassVar[int]
    state: str
    coordinateId: int
    def __init__(self, state: _Optional[str] = ..., coordinateId: _Optional[int] = ...) -> None: ...

class ConnectRequest(_message.Message):
    __slots__ = ("ip",)
    IP_FIELD_NUMBER: _ClassVar[int]
    ip: str
    def __init__(self, ip: _Optional[str] = ...) -> None: ...

class BuffMidsoleRequest(_message.Message):
    __slots__ = ("pos", "dir")
    POS_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    pos: str
    dir: bool
    def __init__(self, pos: _Optional[str] = ..., dir: bool = ...) -> None: ...
