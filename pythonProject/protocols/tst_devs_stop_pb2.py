# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tst_devs_stop.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tst_devs_stop.proto',
  package='protobuf.TST_DEVS_STOP',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13tst_devs_stop.proto\x12\x16protobuf.TST_DEVS_STOP\"G\n\x07Request\x12\x16\n\x0estrAskSoftGuid\x18\x01 \x01(\t\x12\x10\n\x08water_id\x18\x02 \x01(\t\x12\x12\n\nstrDevCode\x18\x03 \x03(\t\"~\n\x07Respond\x12\x13\n\x0bstrDevsName\x18\x01 \x01(\t\x12\x12\n\nstrDevCode\x18\x02 \x01(\t\x12\r\n\x05\x62IsOK\x18\x03 \x01(\x08\x12\x10\n\x08strError\x18\x04 \x01(\t\x12\x17\n\x0fiReferenceCount\x18\x05 \x01(\x05\x12\x10\n\x08water_id\x18\x06 \x01(\tb\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='protobuf.TST_DEVS_STOP.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='strAskSoftGuid', full_name='protobuf.TST_DEVS_STOP.Request.strAskSoftGuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='water_id', full_name='protobuf.TST_DEVS_STOP.Request.water_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strDevCode', full_name='protobuf.TST_DEVS_STOP.Request.strDevCode', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=118,
)


_RESPOND = _descriptor.Descriptor(
  name='Respond',
  full_name='protobuf.TST_DEVS_STOP.Respond',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='strDevsName', full_name='protobuf.TST_DEVS_STOP.Respond.strDevsName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strDevCode', full_name='protobuf.TST_DEVS_STOP.Respond.strDevCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bIsOK', full_name='protobuf.TST_DEVS_STOP.Respond.bIsOK', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strError', full_name='protobuf.TST_DEVS_STOP.Respond.strError', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iReferenceCount', full_name='protobuf.TST_DEVS_STOP.Respond.iReferenceCount', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='water_id', full_name='protobuf.TST_DEVS_STOP.Respond.water_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=246,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Respond'] = _RESPOND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'tst_devs_stop_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.TST_DEVS_STOP.Request)
  })
_sym_db.RegisterMessage(Request)

Respond = _reflection.GeneratedProtocolMessageType('Respond', (_message.Message,), {
  'DESCRIPTOR' : _RESPOND,
  '__module__' : 'tst_devs_stop_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.TST_DEVS_STOP.Respond)
  })
_sym_db.RegisterMessage(Respond)


# @@protoc_insertion_point(module_scope)
