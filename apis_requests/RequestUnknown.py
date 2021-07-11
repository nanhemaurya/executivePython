# RequestUnknown
from ApiHandler import ApiRequestInitiator, ResponseType
from BaseRequestHandler import BaseRequestHandler


class RequestUnknown(BaseRequestHandler):

    def runRequest(self):
        self.response.body = {
            "message": "Invalid request",
            "code": ResponseType.Forbidden.value
        }
        self.setResponse(ResponseType.Forbidden)
