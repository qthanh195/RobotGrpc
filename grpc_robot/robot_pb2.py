# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robot.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0brobot.proto\x12\x05robot\"\x0e\n\x0c\x45mptyRequest\"\x1e\n\rStateResponse\x12\r\n\x05state\x18\x01 \x01(\t\")\n\x12LoadProgramRequest\x12\x13\n\x0bnameProgram\x18\x01 \x01(\t\"9\n\x13LoadProgramResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x13\n\x0bnameProgram\x18\x02 \x01(\t\"\x1d\n\x0eMoveTCPRequest\x12\x0b\n\x03pos\x18\x01 \x01(\t\")\n\tIORequest\x12\x0b\n\x03pin\x18\x01 \x01(\x05\x12\x0f\n\x07ioState\x18\x02 \x01(\x08\";\n\x14ProgramStateResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x14\n\x0cprogramState\x18\x02 \x01(\t\")\n\x0bPosResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x0b\n\x03pos\x18\x02 \x01(\t\"\x1f\n\rToolIdRequest\x12\x0e\n\x06toolId\x18\x01 \x01(\x05\"/\n\x0eToolIdResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x0e\n\x06toolId\x18\x02 \x01(\x05\"+\n\x13\x43oordinateIdRequest\x12\x14\n\x0c\x63oordinateId\x18\x01 \x01(\x05\";\n\x14\x43oordinateIdResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x14\n\x0c\x63oordinateId\x18\x02 \x01(\x05\"\x1c\n\x0e\x43onnectRequest\x12\n\n\x02ip\x18\x01 \x01(\t\".\n\x12\x42uffMidsoleRequest\x12\x0b\n\x03pos\x18\x01 \x01(\t\x12\x0b\n\x03\x64ir\x18\x02 \x01(\x08\x32\xe2\n\n\x05Robot\x12\x38\n\x07\x43onnect\x12\x15.robot.ConnectRequest\x1a\x14.robot.StateResponse\"\x00\x12\x39\n\nDisconnect\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x43\n\x0eRunBuffMidsole\x12\x19.robot.BuffMidsoleRequest\x1a\x14.robot.StateResponse\"\x00\x12\x36\n\x07PowerOn\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x37\n\x08PowerOff\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x35\n\x06\x45nable\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x36\n\x07\x44isable\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x37\n\x08Shutdown\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x34\n\x05Pause\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x35\n\x06Resume\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x33\n\x04Stop\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x37\n\x08MoveHome\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x46\n\x0bLoadProgram\x12\x19.robot.LoadProgramRequest\x1a\x1a.robot.LoadProgramResponse\"\x00\x12\x39\n\nRunProgram\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x38\n\x07MoveTCP\x12\x15.robot.MoveTCPRequest\x1a\x14.robot.StateResponse\"\x00\x12\x31\n\x05SetIO\x12\x10.robot.IORequest\x1a\x14.robot.StateResponse\"\x00\x12\x45\n\x0fGetProgramState\x12\x13.robot.EmptyRequest\x1a\x1b.robot.ProgramStateResponse\"\x00\x12;\n\x0c\x41\x62ortprogram\x12\x13.robot.EmptyRequest\x1a\x14.robot.StateResponse\"\x00\x12\x33\n\x06GetPos\x12\x13.robot.EmptyRequest\x1a\x12.robot.PosResponse\"\x00\x12\x39\n\tSetToolId\x12\x14.robot.ToolIdRequest\x1a\x14.robot.StateResponse\"\x00\x12\x39\n\tGetToolId\x12\x13.robot.EmptyRequest\x1a\x15.robot.ToolIdResponse\"\x00\x12\x45\n\x0fSetCoordinateId\x12\x1a.robot.CoordinateIdRequest\x1a\x14.robot.StateResponse\"\x00\x12\x45\n\x0fGetCoordinateId\x12\x13.robot.EmptyRequest\x1a\x1b.robot.CoordinateIdResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'robot_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTYREQUEST']._serialized_start=22
  _globals['_EMPTYREQUEST']._serialized_end=36
  _globals['_STATERESPONSE']._serialized_start=38
  _globals['_STATERESPONSE']._serialized_end=68
  _globals['_LOADPROGRAMREQUEST']._serialized_start=70
  _globals['_LOADPROGRAMREQUEST']._serialized_end=111
  _globals['_LOADPROGRAMRESPONSE']._serialized_start=113
  _globals['_LOADPROGRAMRESPONSE']._serialized_end=170
  _globals['_MOVETCPREQUEST']._serialized_start=172
  _globals['_MOVETCPREQUEST']._serialized_end=201
  _globals['_IOREQUEST']._serialized_start=203
  _globals['_IOREQUEST']._serialized_end=244
  _globals['_PROGRAMSTATERESPONSE']._serialized_start=246
  _globals['_PROGRAMSTATERESPONSE']._serialized_end=305
  _globals['_POSRESPONSE']._serialized_start=307
  _globals['_POSRESPONSE']._serialized_end=348
  _globals['_TOOLIDREQUEST']._serialized_start=350
  _globals['_TOOLIDREQUEST']._serialized_end=381
  _globals['_TOOLIDRESPONSE']._serialized_start=383
  _globals['_TOOLIDRESPONSE']._serialized_end=430
  _globals['_COORDINATEIDREQUEST']._serialized_start=432
  _globals['_COORDINATEIDREQUEST']._serialized_end=475
  _globals['_COORDINATEIDRESPONSE']._serialized_start=477
  _globals['_COORDINATEIDRESPONSE']._serialized_end=536
  _globals['_CONNECTREQUEST']._serialized_start=538
  _globals['_CONNECTREQUEST']._serialized_end=566
  _globals['_BUFFMIDSOLEREQUEST']._serialized_start=568
  _globals['_BUFFMIDSOLEREQUEST']._serialized_end=614
  _globals['_ROBOT']._serialized_start=617
  _globals['_ROBOT']._serialized_end=1995
# @@protoc_insertion_point(module_scope)