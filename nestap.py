from http.server import HTTPServer

from ServerHandler import Main

main = Main()

if __name__ == '__main__':
    main.runServer(HTTPServer)

