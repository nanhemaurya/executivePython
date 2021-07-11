# BaseRequestHandler
import json

from ApiHandler import ApiRequestInitiator, Response, ResponseType, Method


class Content:
    body: str
    content_length: int


class BaseRequestHandler:
    api_request_initiator = None
    url_key = None
    response = Response()
    method = None

    def __init__(self):
        self.response.body = {}

    def doGet(self, api_request_initiator: ApiRequestInitiator):
        self.unknownRequest()

    def doPost(self, api_request_initiator: ApiRequestInitiator):
        self.unknownRequest()

    def doPUT(self, api_request_initiator: ApiRequestInitiator):
        self.unknownRequest()

    def doPatch(self, api_request_initiator: ApiRequestInitiator):
        self.unknownRequest()

    def doDelete(self, api_request_initiator: ApiRequestInitiator):
        self.unknownRequest()

    def init(self, api_request_initiator: ApiRequestInitiator, url_key: str):
        self.url_key = url_key
        self.api_request_initiator = api_request_initiator
        self.method = api_request_initiator.requestMethod
        self.runRequest()

    def runRequest(self):
        if self.method == Method.POST:
            self.doPost(self.api_request_initiator)
        elif self.method == Method.GET:
            self.doGet(self.api_request_initiator)
        elif self.method == Method.PUT:
            self.doPUT(self.api_request_initiator)
        elif self.method == Method.PATCH:
            self.doPatch(self.api_request_initiator)
        elif self.method == Method.DELETE:
            self.doDelete(self.api_request_initiator)

        else:
            self.unknownRequest()

    def setResponse(self, response_type: ResponseType):
        request_handler = self.api_request_initiator.request_handler
        request_handler.send_response(response_type.value)
        request_handler.send_header('Content-type', self.response.content_type)
        json_response = json.dumps(self.response.body)
        my_str_as_bytes = json_response.encode('utf-8', 'replace')
        request_handler.send_header('Content-Length', str(len(my_str_as_bytes)))
        request_handler.send_header('Connection', 'close')
        request_handler.end_headers()
        return request_handler.wfile.write(my_str_as_bytes)

    def getContent(self):
        content = Content()
        request_handler = self.api_request_initiator.request_handler
        content_length = int(request_handler.headers['Content-Length'])  # <--- Gets the size of data
        post_data_body = request_handler.rfile.read(content_length)  # <--- Gets the data itself
        content.body = post_data_body
        content.content_length = content_length
        return content

    def unknownRequest(self):
        self.response.body = {
            "method": self.api_request_initiator.requestMethod,
            "message": "Method not allowed"
        }
        self.setResponse(ResponseType.BadRequest)
