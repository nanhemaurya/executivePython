# Requests Profile
from ApiHandler import ApiRequestInitiator, ResponseType
from BaseRequestHandler import BaseRequestHandler


class RequestProfile(BaseRequestHandler):

    def doGet(self, api_request_initiator: ApiRequestInitiator):
        self.response.body = {
            "message": "GET method is working"
        }
        self.setResponse(ResponseType.Success)
