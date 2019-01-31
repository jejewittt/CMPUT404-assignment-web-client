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
import urllib
import json



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
        response = None
        print(data)
        response = data.split()[1]
        return int(response)

    def get_headers(self,data):
        response = None 
        return response

    def get_body(self, data):
        # print(3)
        # print(len(data))
        # print(data)
        # print("-----------------------------------")
        c=False
        old1=None
        old2=None
        response = ""
        for i in data:
            if (old1 == '\r' or old2=='\r') and i=='\r':
                c=True
            if c:
                response+=i
            else:   
                old2=old1          
                old1=i
                

        return response
    
    # def encode_arg(self,data):
    #     data = data.replace("\n","%20")
    #     return data
    def sendall(self, data):
        print(888)
        print(data)
        self.socket.sendall(data.encode('utf-8'))
        
    def close(self):
        self.socket.close()

    # read everything from the socket
    def recvall(self, sock):
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
        # print(args)
        try:
            int(urllib.parse.urlsplit(url)[1].split(':')[1])     
            payload = """GET {} HTTP/1.1\r\nHOST: {}\r\n\r\n """.format(urllib.parse.urlsplit(url)[2],url)
            print(111)
            print(url)

            # print(urllib.parse.urlsplit(url)[1].split(':')[1])
            self.connect(urllib.parse.urlsplit(url)[1].split(':')[0],int(urllib.parse.urlsplit(url)[1].split(':')[1]) )
            self.sendall(payload)
            response = self.recvall(self.socket)
            print(222)
            print(response)
            code = self.get_code(response)
            # print(code)
            body = self.get_body(response)
            print(333)
            print(body)
            self.close()
            return HTTPResponse(code, body)
        except IndexError:
            print (7)
            # print(args)
            payload = """GET {} HTTP/1.1\r\nHOST: {} \r\nConnection: close\r\nAccept: */*\r\n\r\n """.format(url,urllib.parse.urlsplit(url)[1].split(':')[0])
            print(111)
            # print(url)
            print(payload)
            # print(urllib.parse.urlsplit(url)[1].split(':')[1])
            print(urllib.parse.urlsplit(url)[1].split(':')[0])
            self.connect(urllib.parse.urlsplit(url)[1].split(':')[0],80)
            # self.connect(urllib.parse.urlsplit(url)[1].split(':')[0],int(urllib.parse.urlsplit(url)[1].split(':')[1]) )
            


            self.sendall(payload)
            response = self.recvall(self.socket)
            # print(222)
            # print(response)
            code = self.get_code(response)
            # print(code)
            body = self.get_body(response)
            # print(333)
            # print(body)
            self.close()
            return HTTPResponse(code, body)

    def POST(self, url, args=None):
        print(8)
        # print("-----------------------------------")
        # print(url)
        # print(args)
        leng = 0
        test=None
        if args:
            leng=0
        goto=urllib.parse.urlsplit(url)[2]
        if args:
            test = ""
            for i in args:
                test+= i + "="+args[i]+'&'
            test = test[:-1]
        # if args:
        #     test= json.dumps(test)
        # print(234234)
        # print(urllib.parse.quote(test,safe=''))
        if test:
            leng = len(test)
        # print(url)
        payload = """POST {} HTTP/1.1\r\nHOST: {} \r\nContent-Length: {} \r\n\r\n{}""".format(goto,url,leng,test)
        # print(urllib.parse.urlsplit(url)[1].split(':'))
        self.connect(urllib.parse.urlsplit(url)[1].split(':')[0],int(urllib.parse.urlsplit(url)[1].split(':')[1]))
        self.sendall(payload)
        response = self.recvall(self.socket)
        # print(response)
        code = self.get_code(response)
        body = self.get_body(response)
        # print("aawdawdawdawd")
        # print("-----------response---------------")
        # print(body)
        # print("--------------------------")

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
