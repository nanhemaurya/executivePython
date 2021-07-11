import requests


class Script:
    __run = True

    _number = None
    _password = None

    def __init__(self, number, password):
        print("initiated")
        self._number = number
        self._password = password

    def getToken(self):
        req = requests.post(
            "https://allcaps.co.in/api/token/",
            data={"phone": self._number, "password": self._password}
        )

        print(req.content.decode("utf-8"))
        self.__run = False

    def getRun(self):
        return self.__run
