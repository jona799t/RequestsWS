import websocket #pip install websocket-client

import gzip
import json as JSON

import time
import timeout_decorator

import threading

import difflib

def iniziateConnection(wsURL):
    ws = websocket.WebSocket()
    ws.connect(wsURL)
    return websocket.WebSocket()


def closeConnection(ws):
    ws.close()

ws = websocket.WebSocket()
wsData = {"CURRENT_URL": None}

lastResponse = ""
class get:
    def __init__(self, wsUrl, timeout=None):
        global lastResponse

        self.Error = False
        if wsUrl != wsData["CURRENT_URL"]:
            ws.connect(wsUrl)

        @timeout_decorator.timeout(timeout if timeout != 0 else 10**-100)
        def funcWaitForResponse():
            while True:
                response = ws.recv()
                #print('\n'.join(difflib.ndiff([response], [lastResponse])))
                if lastResponse != response:
                    return response

        self.text = funcWaitForResponse()
        lastResponse = self.text

    def json(self):
        if not self.Error:
            return JSON.loads(self.text)
        else:
            return {"ERROR_MESSAGE": self.text}

class post:
    def __init__(self, wsUrl, data=None, json=None, waitForResponse=True, timeout=None):
        global lastResponse

        self.Error = False

        if wsUrl != wsData["CURRENT_URL"]:
            ws.connect(wsUrl)

        if data == None and json == None:
            self.text = "RequestsWS | Error #1: data or json is needed"
            self.Error = True
            return

        @timeout_decorator.timeout(timeout if timeout != 0 else 10**-100)
        def funcWaitForResponse():
            while True:
                response = ws.recv()
                #print('\n'.join(difflib.ndiff([response], [lastResponse])))
                if lastResponse != response:
                    print("Not the same")
                    return response

        if waitForResponse:
            try:
                self.text = funcWaitForResponse()

                lastResponse = self.text
            except timeout_decorator.timeout_decorator.TimeoutError:
                self.text = "RequestsWS | Error #2: request timed out"
                self.Error = True
                return


        dataFormatted = JSON.dumps(data) if type(data) == dict else data if data != None else JSON.dumps(json)

        if waitForResponse:
            ws.send(dataFormatted)
            self.text = ws.recv()

    def json(self):
        if not self.Error:
            return JSON.loads(self.text)
        else:
            return {"ERROR_MESSAGE": self.text}

def keepWSConnection(wsUrl, interval, payload, ws):
    while True:
        if wsData["CURRENT_URL"] == wsUrl:
            time.sleep(interval)
            ws.send(payload)
        else:
            print("New website, stopping the pings")

class keepConnection:
    def __init__(self, wsUrl, interval, data=None, json=None):
        if data == None and json == None:
            self.text = "RequestsWS | Error #1: data or json is needed"
            self.Error = True
            return

        dataFormatted = JSON.dumps(data) if type(data) == dict else data if data != None else JSON.dumps(json)
        threading._start_new_thread(keepConnection, (wsUrl, interval, dataFormatted, ws))
