# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chat_pb2 as chat__pb2


class ChatStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConversaChat = channel.unary_stream(
                '/Chat/ConversaChat',
                request_serializer=chat__pb2.Retorno.SerializeToString,
                response_deserializer=chat__pb2.Mensagem.FromString,
                )
        self.EnviaMensagem = channel.unary_unary(
                '/Chat/EnviaMensagem',
                request_serializer=chat__pb2.Mensagem.SerializeToString,
                response_deserializer=chat__pb2.Retorno.FromString,
                )


class ChatServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ConversaChat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnviaMensagem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ConversaChat': grpc.unary_stream_rpc_method_handler(
                    servicer.ConversaChat,
                    request_deserializer=chat__pb2.Retorno.FromString,
                    response_serializer=chat__pb2.Mensagem.SerializeToString,
            ),
            'EnviaMensagem': grpc.unary_unary_rpc_method_handler(
                    servicer.EnviaMensagem,
                    request_deserializer=chat__pb2.Mensagem.FromString,
                    response_serializer=chat__pb2.Retorno.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Chat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Chat(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ConversaChat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Chat/ConversaChat',
            chat__pb2.Retorno.SerializeToString,
            chat__pb2.Mensagem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnviaMensagem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Chat/EnviaMensagem',
            chat__pb2.Mensagem.SerializeToString,
            chat__pb2.Retorno.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
