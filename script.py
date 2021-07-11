import json

import requests


class Token:
    refresh = None
    access = None
    user_guid = None
    user_name = None

    def __init__(self, refresh, access, user_guid, user_name):
        self.refresh = refresh
        self.access = access
        self.user_guid = user_guid
        self.user_name = user_name


def getHeader(access_token):
    return {
        "Authorization": f"JWT {access_token}",
        "Content-Type": "application/json"
    }


class Script:
    __baseUrl = "https://allcaps.co.in/api/"

    __run = True

    _number = None
    _password = None

    def __init__(self, number, password):
        print("initiated")
        self._number = number
        self._password = password

    def getToken(self):
        req = requests.post(
            f"{self.__baseUrl}token/",
            data={"phone": self._number, "password": self._password}
        )
        res = json.loads(req.content.decode("utf-8"))
        self.__run = False
        return Token(
            res["refresh"],
            res["access"],
            res["data"]["user_guid"],
            res["data"]["user_name"]
        )

    def fetchToken(self):
        req = requests.post(
            f"{self.__baseUrl}token/",
            data={"phone": self._number, "password": self._password}
        )
        return json.loads(req.content.decode("utf-8"))

    def getRun(self):
        return self.__run

    def fetchStaff(self, user_guid, access_token):
        url = f"{self.__baseUrl}staff/{user_guid}/"
        req = requests.get(
            url=url,
            headers=getHeader(access_token)
        )
        return json.loads(req.content.decode("utf-8"))

    def getStaff(self, user_guid, access_token):
        url = f"{self.__baseUrl}staff/{user_guid}/"
        req = requests.get(
            url=url,
            headers=getHeader(access_token)
        )
        res = json.loads(req.content.decode("utf-8"))
        print(json.dumps(res, indent=4, sort_keys=True))
        # print(res)
