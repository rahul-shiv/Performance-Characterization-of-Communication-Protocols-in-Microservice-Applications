# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc

import image_pb2_grpc
import image_pb2

import base64
import sys
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    number = int(sys.argv[1])

    def process_response(call_future):
        print(call_future.result())
    
    with open("4k.jpeg","rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    # encoded_string = b'abcd'
    # print(sys.getsizeof(encoded_string))
    while(number):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = image_pb2_grpc.GreeterStub(channel)
            response = stub.Send(image_pb2.Request(req_content=encoded_string))
        number = number - 1

            # if number%2:
            #     response = stub.Send.future(image_pb2.Request(req_content=str(number).encode()))
            #     response.add_done_callback(process_response)
            # elif number%2==0:
            #     response = stub.Send.future(image_pb2.Request(req_content=encoded_string))
            #     response.add_done_callback(process_response)
            # print(response.resp_content,end=',')
    #print("Greeter client received: " + response.resp_content)

if __name__ == '__main__':
    logging.basicConfig()
    run()
