# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SZDFH-TST.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SZDFH-TST.proto',
  package='protobuf',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fSZDFH-TST.proto\x12\x08protobuf\"\x8d\x01\n\tTST_LOGIN\x12\x13\n\x0bstrSoftCode\x18\x01 \x01(\t\x12\x13\n\x0bstrSoftGuid\x18\x02 \x01(\t\x12\x11\n\tstrUserID\x18\x03 \x01(\t\x12\x13\n\x0bstrUserName\x18\x04 \x01(\t\x12\x16\n\x0estrSoftLocalIP\x18\x05 \x01(\t\x12\x16\n\x0eiSoftLocalPort\x18\x06 \x01(\x05\"\x8e\x01\n\nTST_LOGOFF\x12\x13\n\x0bstrSoftCode\x18\x01 \x01(\t\x12\x13\n\x0bstrSoftGuid\x18\x02 \x01(\t\x12\x11\n\tstrUserID\x18\x03 \x01(\t\x12\x13\n\x0bstrUserName\x18\x04 \x01(\t\x12\x16\n\x0estrSoftLocalIP\x18\x05 \x01(\t\x12\x16\n\x0eiSoftLocalPort\x18\x06 \x01(\x05\x62\x06proto3'
)




_TST_LOGIN = _descriptor.Descriptor(
  name='TST_LOGIN',
  full_name='protobuf.TST_LOGIN',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='strSoftCode', full_name='protobuf.TST_LOGIN.strSoftCode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strSoftGuid', full_name='protobuf.TST_LOGIN.strSoftGuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strUserID', full_name='protobuf.TST_LOGIN.strUserID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strUserName', full_name='protobuf.TST_LOGIN.strUserName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strSoftLocalIP', full_name='protobuf.TST_LOGIN.strSoftLocalIP', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iSoftLocalPort', full_name='protobuf.TST_LOGIN.iSoftLocalPort', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=30,
  serialized_end=171,
)


_TST_LOGOFF = _descriptor.Descriptor(
  name='TST_LOGOFF',
  full_name='protobuf.TST_LOGOFF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='strSoftCode', full_name='protobuf.TST_LOGOFF.strSoftCode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strSoftGuid', full_name='protobuf.TST_LOGOFF.strSoftGuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strUserID', full_name='protobuf.TST_LOGOFF.strUserID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strUserName', full_name='protobuf.TST_LOGOFF.strUserName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strSoftLocalIP', full_name='protobuf.TST_LOGOFF.strSoftLocalIP', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iSoftLocalPort', full_name='protobuf.TST_LOGOFF.iSoftLocalPort', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=174,
  serialized_end=316,
)

DESCRIPTOR.message_types_by_name['TST_LOGIN'] = _TST_LOGIN
DESCRIPTOR.message_types_by_name['TST_LOGOFF'] = _TST_LOGOFF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TST_LOGIN = _reflection.GeneratedProtocolMessageType('TST_LOGIN', (_message.Message,), {
  'DESCRIPTOR' : _TST_LOGIN,
  '__module__' : 'SZDFH_TST_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.TST_LOGIN)
  })
_sym_db.RegisterMessage(TST_LOGIN)

TST_LOGOFF = _reflection.GeneratedProtocolMessageType('TST_LOGOFF', (_message.Message,), {
  'DESCRIPTOR' : _TST_LOGOFF,
  '__module__' : 'SZDFH_TST_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.TST_LOGOFF)
  })
_sym_db.RegisterMessage(TST_LOGOFF)


# @@protoc_insertion_point(module_scope)