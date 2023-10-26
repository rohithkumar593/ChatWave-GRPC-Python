import chatting_service_pb2_grpc, chat_request_response_pb2, grpc, asyncio
from src.helpers import get_inputs, run_two_functions, get_receivers_id
from src.constants import ChatCodes


def send_text(senders_id, receivers_id, message_update, status, stub):
    reply = stub.ping(
        chat_request_response_pb2.sendtext(
            senders_id=senders_id,
            receivers_id=receivers_id,
            message_update=message_update,
            status=status,
        )
    )

    for data in reply:
        print(data)


def get_inputs_and_run_stub(senders_id, stub):
    data, receivers_id = get_inputs()
    send_text(
        senders_id=senders_id,
        receivers_id=receivers_id,
        message_update=data,
        stub=stub,
        status=ChatCodes.SEND_MESSAGE,
    )


def run_stream_server_response4(address: str, senders_id: str):
    with grpc.insecure_channel(address) as channel:
        stub = chatting_service_pb2_grpc.chatmanageStub(channel)
        try:
            send_text(
                senders_id=senders_id,
                receivers_id="",
                message_update="",
                status=ChatCodes.LOAD_MESSAGES,
                stub=stub,
            )
            get_inputs_and_run_stub(senders_id=senders_id, stub=stub)

        except grpc.RpcError as rpc_error:
            if (
                rpc_error.code() != grpc.StatusCode.CANCELLED
                or rpc_error.code() != grpc.StatusCode.UNAVAILABLE
            ):
                print(
                    f"Received unknown RPC error: code={rpc_error.code()} message={rpc_error.details()}"
                )


def run_unary_request(address: str, senders_id: str):
    with grpc.insecure_channel(address) as channel:
        receivers_id = get_receivers_id()
        stub = chatting_service_pb2_grpc.chatmanageStub(channel)
        try:
            reply = stub.lastseen(
                chat_request_response_pb2.checkonlinestatus(
                    senders_id=senders_id, receivers_id=receivers_id
                )
            )
            print(type(reply), reply.lastseen)
        except grpc.RpcError as rpc_error:
            if (
                rpc_error.code() != grpc.StatusCode.CANCELLED
                or rpc_error.code() != grpc.StatusCode.UNAVAILABLE
            ):
                print(
                    f"Received unknown RPC error: code={rpc_error.code()} message={rpc_error.details()}"
                )
