# RequestProfile
import json

import script
from ApiHandler import ApiRequestInitiator, ResponseType
from BaseRequestHandler import BaseRequestHandler


class RequestToken(BaseRequestHandler):

    def doPost(self, api_request_initiator: ApiRequestInitiator):
        content = self.getContent()
        json_data = (content.body.decode("utf-8"))
        body = json.loads(json_data)
        self.response.body = body
        scr = script.Script(body["phone"], body["password"])

        # res.body = scr.fetchToken()
        token = scr.fetchToken()
        self.response.body = scr.fetchStaff(token["data"]["user_guid"], token["access"])
        self.setResponse(ResponseType.Success)
