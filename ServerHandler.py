# Server Handler
import json
import logging
import os
import sys
from http.server import BaseHTTPRequestHandler
from ApiHandler import ApiHandler, Method
from apis_requests.RequestProfile import RequestProfile
from apis_requests.RequestToken import RequestToken
from apis_requests.RequestUnknown import RequestUnknown

config_file_name = f"{os.path.abspath(os.path.dirname(sys.argv[0]))}/config.json"
port: int = 1234


class ApiRequestHandler:
    __api_requests = {}

    def __init__(self):
        self.__initApisRequestsHandler()

    def __initApisRequestsHandler(self):
        self.__setRequest("profile", RequestProfile())
        self.__setRequest("token", RequestToken())
        self.__setRequest("unknown", RequestUnknown())

    def __setRequest(self, key, request_handler):
        self.__api_requests[key] = request_handler

    def getRequest(self, key):
        return self.__api_requests[key]


class S(BaseHTTPRequestHandler):
    api_requests: ApiRequestHandler = None

    def do_GET(self):
        ApiHandler(self, Method.GET)

    def do_POST(self):
        ApiHandler(self, Method.POST)

    def getRequest(self, key):
        return self.api_requests.getRequest(key)

    def send_error(self, code, message=None, explain=None):
        if self.command is not None:
            ApiHandler(self, self.command.upper())
        else:
            if self.command != 'HEAD':
                ApiHandler(self, Method.GET)


class Config:
    port: int = port


class Main:
    __config = None
    __api_requests = None

    def __init__(self):
        self.setFileConfig()
        self.initApisRequestsHandler()

    def setFileConfig(self):
        # Python program to read
        # json file
        # Opening JSON file

        config = Config()
        try:
            f = open(config_file_name, 'r')
            # returns JSON object as
            # a dictionary
            data = json.load(f)
            config.port = port if (data["port"] is None) else data["port"]
            # Closing file
            f.close()

        except:
            print(f"{config_file_name} not found...")

        self.__config = config

    def getConfig(self):
        return self.__config

    def runServer(self, server_class):
        base_class = S
        base_class.api_requests = self.__api_requests
        logging.basicConfig(level=logging.INFO)
        server_address = ('', self.getConfig().port)
        httpd = server_class(server_address, base_class)
        logging.info(f'Starting httpd... at port:{self.getConfig().port}\n')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        logging.info('Stopping httpd...\n')

    def initApisRequestsHandler(self):
        self.__api_requests = ApiRequestHandler()
