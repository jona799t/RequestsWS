import websocket #pip install websocket-client

import gzip
import json as JSON

def iniziateConnection(wsURL):
    ws = websocket.WebSocket()
    ws.connect(wsURL)
    return websocket.WebSocket()


def closeConnection(ws):
    ws.close()


def get(ws, encoding=None):
    if encoding == "gzip":
        responseFormatted = str(gzip.decompress(ws.recv()), encoding="utf8")
    else:
        responseFormatted = str(ws.recv(), encoding="utf8")

    def json():
        return JSON.loads(responseFormatted)


def post(ws, data=None, json=None):
    if data == None and json == None:
        print(f"requestWS | Error #1: data or json is needed")
        exit()

    dataFormatted = JSON.dumps(data) if type(data) == dict else data if data != None else JSON.dumps(
        json)

    ws.send(dataFormatted)

    def response(compression=None, encoding=None):
        encodingFormated = "utf8" if encoding == None else encoding
        if compression == "gzip":
            responseFormatted = str(gzip.decompress(ws.recv()), encoding=encodingFormated)
        else:
            responseFormatted = str(ws.recv(), encoding=encodingFormated)

        def json():
            return JSON.loads(responseFormatted)

WS = websocket.WebSocket()
class Session:
    def __init__(self, wsURL, proxy=None):
        self.Proxy = proxy
        self.WS = websocket.WebSocket()
        self.WS.connect(wsURL)
        global WS
        WS = self.WS
        print(self.WS.recv())

    def closeConnection(self):
        self.WS.close()

    def get(self, encoding=None):
        if encoding == "gzip":
            responseFormatted = str(gzip.decompress(self.WS.recv()), encoding="utf8")
        else:
            responseFormatted = str(self.WS.recv(), encoding="utf8")

        return responseFormatted

        def json():
            return JSON.loads(responseFormatted)

    class post:
        def __init__(self, data=None, json=None, waitForResponse=True, compression=None, encoding=None):
            global WS
            self.WS = WS
            if data == None and json == None:
                print(f"RequestWS | Error #1: data or json is needed")
                exit()

            dataFormatted = JSON.dumps(data) if type(data) == dict else data if data != None else JSON.dumps(json)

            self.WS.send(dataFormatted)

            if waitForResponse:
                encodingFormated = "utf8" if encoding == None else encoding
                if compression == "gzip":
                    self.text = str(gzip.decompress(self.WS.recv()), encoding=encodingFormated)
                elif compression == "json":
                    self.json = JSON.loads(str(self.WS.recv()))
                else:
                    self.text = str(self.WS.recv())

        def response(self, compression=None, encoding=None):
            encodingFormated = "utf8" if encoding == None else encoding
            if compression == "gzip":
                responseFormatted = str(gzip.decompress(self.WS.recv()), encoding=encodingFormated)
            elif compression == "json":
                responseFormatted = JSON.loads(str(self.WS.recv()))
            else:
                responseFormatted = str(self.WS.recv())

            return responseFormatted

        def json(self):
            return JSON.loads(self.responseFormatted)
