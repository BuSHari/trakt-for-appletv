# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UpdateClientMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ProtocolMessage_pb2 as ProtocolMessage__pb2
from . import NowPlayingClient_pb2 as NowPlayingClient__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='UpdateClientMessage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x19UpdateClientMessage.proto\x1a\x15ProtocolMessage.proto\x1a\x16NowPlayingClient.proto\"8\n\x13UpdateClientMessage\x12!\n\x06\x63lient\x18\x01 \x01(\x0b\x32\x11.NowPlayingClient:C\n\x13updateClientMessage\x12\x10.ProtocolMessage\x18; \x01(\x0b\x32\x14.UpdateClientMessage')
  ,
  dependencies=[ProtocolMessage__pb2.DESCRIPTOR,NowPlayingClient__pb2.DESCRIPTOR,])


UPDATECLIENTMESSAGE_FIELD_NUMBER = 59
updateClientMessage = _descriptor.FieldDescriptor(
  name='updateClientMessage', full_name='updateClientMessage', index=0,
  number=59, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_UPDATECLIENTMESSAGE = _descriptor.Descriptor(
  name='UpdateClientMessage',
  full_name='UpdateClientMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client', full_name='UpdateClientMessage.client', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=132,
)

_UPDATECLIENTMESSAGE.fields_by_name['client'].message_type = NowPlayingClient__pb2._NOWPLAYINGCLIENT
DESCRIPTOR.message_types_by_name['UpdateClientMessage'] = _UPDATECLIENTMESSAGE
DESCRIPTOR.extensions_by_name['updateClientMessage'] = updateClientMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateClientMessage = _reflection.GeneratedProtocolMessageType('UpdateClientMessage', (_message.Message,), dict(
  DESCRIPTOR = _UPDATECLIENTMESSAGE,
  __module__ = 'UpdateClientMessage_pb2'
  # @@protoc_insertion_point(class_scope:UpdateClientMessage)
  ))
_sym_db.RegisterMessage(UpdateClientMessage)

updateClientMessage.message_type = _UPDATECLIENTMESSAGE
ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(updateClientMessage)

# @@protoc_insertion_point(module_scope)
