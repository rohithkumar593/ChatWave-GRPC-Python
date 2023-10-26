import chat_request_response_pb2, chatting_service_pb2_grpc, asyncio
from collections import defaultdict
from datetime import datetime
from src.constants import Status, ChatCodes


class ChatServicer(chatting_service_pb2_grpc.chatmanageServicer):
    def __init__(self):
        self.message_hash = defaultdict(lambda: asyncio.Queue())
        self.last_seen = defaultdict(str)

    async def ping(self, request, context):
        await self.update_last_seen(id=request.senders_id)

        if request.status == ChatCodes.LOAD_MESSAGES:
            while not self.message_hash[request.senders_id].empty():
                yield chat_request_response_pb2.receiveacknowledgment(
                    message_status=Status.SENT,
                    message=await self.message_hash[request.senders_id].get(),
                )
        elif request.status == ChatCodes.SEND_MESSAGE:
            if request.message_update != "":
                await self.message_hash[request.receivers_id].put(
                    request.message_update
                )
            while not self.message_hash[request.senders_id].empty():
                yield chat_request_response_pb2.receiveacknowledgment(
                    message_status=Status.SENT,
                    message=await self.message_hash[request.senders_id].get(),
                )
        

    async def lastseen(self, request, context):
        last_seen = self.last_seen[request.receivers_id]
        if last_seen:
            last_seen = (
                Status.ONLINE
                if (datetime.now() - last_seen).seconds < Status.FEASIBLE_TIME
                else f"{Status.LAST_SEEN_AT} {last_seen}"
            )
        await self.update_last_seen(request.senders_id)
        return chat_request_response_pb2.receivestatus(lastseen=last_seen)

    async def update_last_seen(self, id):
        self.last_seen[id] = datetime.now()
