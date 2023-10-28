
# ChatWave-GRPC-Python
This repository contains the backend source code for Chat Service.  Key Features:   1. Users can message each other 2. Users will be able to see the last seen/Online status of Receiver.            GRPC Protocol - This Chat Service is developed using GRPC Protocol, and server uses asynchronous mechanism to talk with clients, Tech stack : Python

Design Used For Chat Service ( Only 1 Receiver is shown, Can be extended to multiple receivers)



![image](https://github.com/rohithkumar593/ChatWave-GRPC-Python/assets/54279129/1a3cbeb9-5bfa-42b7-a54a-ccd763ae9a39)


Installation Steps:

1. Create Virtual Environment - python3 -m venv venv

2. Activate Virtual Environment - source venv/bin/activate

3. Installing Requirements - pip -r ./requirements.txt

4. Run Proto Files -

        1. python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/chatting_service.proto 

        2.python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/chat_request_response.proto

5. Run Server - python3 -m server

6. Open Seperate Terminal and run client1 - python3 -m clients.client1

7. Add one more terminal and run client2 - python3 -m clients.client2

