# Handling Apis Here
import enum


class Method:
    GET = "GET"
    POST = "POST"
    PUT = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"


class Response:
    body: dict
    content_type: str = 'application/json'


class ResponseType(enum.Enum):
    Success = 200
    BadRequest = 400
    Unauthorized = 401
    Forbidden = 403
    NotFound = 404


class ApiRequestInitiator:
    url = None
    requestMethod = None
    request_handler = None


class ApiHandler:
    __url: str = None
    __requestMethod = None
    __request_handler = None

    __api_requests = None

    def __init__(self, handler, method):
        self.__api_requests = handler.api_requests
        self.__url = handler.path
        self.__request_handler = handler
        self.__requestMethod = method
        self.handlerApi()

    def handlerApi(self):
        api_req_init = ApiRequestInitiator()
        api_req_init.url = self.__url
        api_req_init.request_handler = self.__request_handler
        api_req_init.requestMethod = self.__requestMethod

        try:
            url_key = self.__url.split("/")[1]
            req = self.__request_handler.getRequest(url_key)
            if req is not None:
                req.init(api_req_init, url_key)
            else:
                req = self.__request_handler.getRequest("unknown")
                req.init(api_req_init, url_key)
        except:
            self.__request_handler.getRequest("unknown").init(api_req_init, 'unknown')
