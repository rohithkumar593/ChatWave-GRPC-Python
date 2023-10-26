from concurrent import futures
import grpc
import chatting_service_pb2_grpc
from datetime import datetime as time
from src.services.chat_servicer import ChatServicer
import asyncio
from src.config import config


async def serve(address):
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    chatting_service_pb2_grpc.add_chatmanageServicer_to_server(ChatServicer(), server)
    server.add_insecure_port(address)
    await server.start()
    await server.wait_for_termination()


asyncio.run(serve(config.address))
