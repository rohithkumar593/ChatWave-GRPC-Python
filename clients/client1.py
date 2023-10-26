from client import run_stream_server_response4
from src.config import config


run_stream_server_response4(address=config.address, senders_id=config.clients[0])

# run_unary_request(
#     address= config.address,
#     senders_id=config.clients[0]
# )
