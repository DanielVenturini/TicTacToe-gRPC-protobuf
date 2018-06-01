# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Agenda.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Agenda.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x41genda.proto\")\n\x07\x43ontato\x12\x0c\n\x04nome\x18\x01 \x02(\t\x12\x10\n\x08telefone\x18\x02 \x02(\t2o\n\x06\x41genda\x12!\n\tAdicionar\x12\x08.Contato\x1a\x08.Contato\"\x00\x12\x1f\n\x07Remover\x12\x08.Contato\x1a\x08.Contato\"\x00\x12!\n\tConsultar\x12\x08.Contato\x1a\x08.Contato\"\x00')
)




_CONTATO = _descriptor.Descriptor(
  name='Contato',
  full_name='Contato',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='Contato.nome', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telefone', full_name='Contato.telefone', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=16,
  serialized_end=57,
)

DESCRIPTOR.message_types_by_name['Contato'] = _CONTATO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Contato = _reflection.GeneratedProtocolMessageType('Contato', (_message.Message,), dict(
  DESCRIPTOR = _CONTATO,
  __module__ = 'Agenda_pb2'
  # @@protoc_insertion_point(class_scope:Contato)
  ))
_sym_db.RegisterMessage(Contato)



_AGENDA = _descriptor.ServiceDescriptor(
  name='Agenda',
  full_name='Agenda',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=59,
  serialized_end=170,
  methods=[
  _descriptor.MethodDescriptor(
    name='Adicionar',
    full_name='Agenda.Adicionar',
    index=0,
    containing_service=None,
    input_type=_CONTATO,
    output_type=_CONTATO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Remover',
    full_name='Agenda.Remover',
    index=1,
    containing_service=None,
    input_type=_CONTATO,
    output_type=_CONTATO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Consultar',
    full_name='Agenda.Consultar',
    index=2,
    containing_service=None,
    input_type=_CONTATO,
    output_type=_CONTATO,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENDA)

DESCRIPTOR.services_by_name['Agenda'] = _AGENDA

# @@protoc_insertion_point(module_scope)
