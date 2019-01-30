#!/usr/bin/env python3
# coding: utf-8
# Copyright 2016 Abram Hindle, https://github.com/tywtyw2002, and https://github.com/treedust
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

# Do not use urllib's HTTP GET and POST mechanisms.
# Write your own HTTP GET and POST
# The point is to understand what you have to send and get experience with it

import sys
import socket
import re
# you may use urllib to encode data appropriately
import urllib.parse 




def help():
    print("httpclient.py [GET/POST] [URL]\n")

class HTTPResponse(object):
    def __init__(self, code=200, body=""):
        self.code = code
        self.body = body

class HTTPClient(object):
    #def get_host_port(self,url):

    def connect(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        return None

    def get_code(self, data):
        print(1)
        return None

    def get_headers(self,data):
        print(2)
        return None

    def get_body(self, data):
        print(3)
        return None
    
    def sendall(self, data):
        self.socket.sendall(data.encode('utf-8'))
        print(4)
        
    def close(self):
        self.socket.close()
        print(5)

    # read everything from the socket
    def recvall(self, sock):
        print(6)
        buffer = bytearray()
        done = False
        while not done:
            part = sock.recv(1024)
            if (part):
                buffer.extend(part)
            else:
                done = not part
        return buffer.decode('utf-8')

    def GET(self, url, args=None):
        print (7)
        payload = """GET / HTTP/1.1\r\nHOST: {}\r\n\r\n""".format(url)
        print(url)
        self.connect("www.google.com",80)
        print("ad")
        print(urllib.parse.urlsplit(url)[1].split(':')[1])
        self.connect(url,0 )
        test = print("yelp")
        print(test)
        self.s.shutdown(socket.SHUT_WR)
        self.s.close()
        # addr_info = socket.getaddrinfo(HOST, PORT)
        # print("yes")
        # addr = None
        # for addr in addr_info:
        #     if family  == socket.AF_INET and socktype == socket.SOCK_STREAM:
        #         break 

        # try:
        #     s = socket.socket(family,socktype,proto) #good to put into try accept
        #     s.connect(sockaddr)
        #     s.sendall(payload.encode())
        #     s.shutdown(socket.SHUT_WR)
        #     full_data = b""
        #     while True:
        #         data = s.recv(BUFFER_SIZE)
        #         if not data: break
        #         full_data+= data
        #     print(full_data)
        # except Exception as e:
        #     print(e)
        #     print("error")
        # finally:
        #     s.close()


        print("this came through ok")



        code = 500
        body = "this was good"
        return HTTPResponse(code, body)









    def POST(self, url, args=None):
        print(8)
        code = 500
        body = ""
        return HTTPResponse(code, body)

    def command(self, url, command="GET", args=None):
        print(9)
        if (command == "POST"):
            return self.POST( url, args )
        else:
            return self.GET( url, args )

if __name__ == "__main__":
    client = HTTPClient()
    command = "GET"
    if (len(sys.argv) <= 1):
        help()
        sys.exit(1)
    elif (len(sys.argv) == 3):
        print(client.command( sys.argv[2], sys.argv[1] ))
    else:
        print(client.command( sys.argv[1] ))
