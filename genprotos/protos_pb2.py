# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos.proto

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
  name='protos.proto',
  package='quiz',
  serialized_pb=_b('\n\x0cprotos.proto\x12\x04quiz\"\xf7\x02\n\tQuizProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x33\n\x08question\x18\x02 \x03(\x0b\x32!.quiz.QuizProto.QuizQuestionProto\x1a\xa6\x02\n\x11QuizQuestionProto\x12\x10\n\x08question\x18\x01 \x02(\t\x12M\n\x04type\x18\x02 \x01(\x0e\x32..quiz.QuizProto.QuizQuestionProto.QuestionType:\x0fMULTIPLE_CHOICE\x12\x41\n\x06\x61nswer\x18\x03 \x03(\x0b\x32\x31.quiz.QuizProto.QuizQuestionProto.QuizAnswerProto\x1a\x35\n\x0fQuizAnswerProto\x12\x0e\n\x06\x61nswer\x18\x01 \x02(\t\x12\x12\n\nis_correct\x18\x02 \x02(\x08\"6\n\x0cQuestionType\x12\x13\n\x0fMULTIPLE_CHOICE\x10\x01\x12\x11\n\rFREE_RESPONSE\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_QUIZPROTO_QUIZQUESTIONPROTO_QUESTIONTYPE = _descriptor.EnumDescriptor(
  name='QuestionType',
  full_name='quiz.QuizProto.QuizQuestionProto.QuestionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE_CHOICE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FREE_RESPONSE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=344,
  serialized_end=398,
)
_sym_db.RegisterEnumDescriptor(_QUIZPROTO_QUIZQUESTIONPROTO_QUESTIONTYPE)


_QUIZPROTO_QUIZQUESTIONPROTO_QUIZANSWERPROTO = _descriptor.Descriptor(
  name='QuizAnswerProto',
  full_name='quiz.QuizProto.QuizQuestionProto.QuizAnswerProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer', full_name='quiz.QuizProto.QuizQuestionProto.QuizAnswerProto.answer', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_correct', full_name='quiz.QuizProto.QuizQuestionProto.QuizAnswerProto.is_correct', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=342,
)

_QUIZPROTO_QUIZQUESTIONPROTO = _descriptor.Descriptor(
  name='QuizQuestionProto',
  full_name='quiz.QuizProto.QuizQuestionProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question', full_name='quiz.QuizProto.QuizQuestionProto.question', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='quiz.QuizProto.QuizQuestionProto.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer', full_name='quiz.QuizProto.QuizQuestionProto.answer', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_QUIZPROTO_QUIZQUESTIONPROTO_QUIZANSWERPROTO, ],
  enum_types=[
    _QUIZPROTO_QUIZQUESTIONPROTO_QUESTIONTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=398,
)

_QUIZPROTO = _descriptor.Descriptor(
  name='QuizProto',
  full_name='quiz.QuizProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='quiz.QuizProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='question', full_name='quiz.QuizProto.question', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_QUIZPROTO_QUIZQUESTIONPROTO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=398,
)

_QUIZPROTO_QUIZQUESTIONPROTO_QUIZANSWERPROTO.containing_type = _QUIZPROTO_QUIZQUESTIONPROTO
_QUIZPROTO_QUIZQUESTIONPROTO.fields_by_name['type'].enum_type = _QUIZPROTO_QUIZQUESTIONPROTO_QUESTIONTYPE
_QUIZPROTO_QUIZQUESTIONPROTO.fields_by_name['answer'].message_type = _QUIZPROTO_QUIZQUESTIONPROTO_QUIZANSWERPROTO
_QUIZPROTO_QUIZQUESTIONPROTO.containing_type = _QUIZPROTO
_QUIZPROTO_QUIZQUESTIONPROTO_QUESTIONTYPE.containing_type = _QUIZPROTO_QUIZQUESTIONPROTO
_QUIZPROTO.fields_by_name['question'].message_type = _QUIZPROTO_QUIZQUESTIONPROTO
DESCRIPTOR.message_types_by_name['QuizProto'] = _QUIZPROTO

QuizProto = _reflection.GeneratedProtocolMessageType('QuizProto', (_message.Message,), dict(

  QuizQuestionProto = _reflection.GeneratedProtocolMessageType('QuizQuestionProto', (_message.Message,), dict(

    QuizAnswerProto = _reflection.GeneratedProtocolMessageType('QuizAnswerProto', (_message.Message,), dict(
      DESCRIPTOR = _QUIZPROTO_QUIZQUESTIONPROTO_QUIZANSWERPROTO,
      __module__ = 'protos_pb2'
      # @@protoc_insertion_point(class_scope:quiz.QuizProto.QuizQuestionProto.QuizAnswerProto)
      ))
    ,
    DESCRIPTOR = _QUIZPROTO_QUIZQUESTIONPROTO,
    __module__ = 'protos_pb2'
    # @@protoc_insertion_point(class_scope:quiz.QuizProto.QuizQuestionProto)
    ))
  ,
  DESCRIPTOR = _QUIZPROTO,
  __module__ = 'protos_pb2'
  # @@protoc_insertion_point(class_scope:quiz.QuizProto)
  ))
_sym_db.RegisterMessage(QuizProto)
_sym_db.RegisterMessage(QuizProto.QuizQuestionProto)
_sym_db.RegisterMessage(QuizProto.QuizQuestionProto.QuizAnswerProto)


# @@protoc_insertion_point(module_scope)
