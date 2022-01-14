from websocket import create_connection
import json as JSON

import threading
from cancelable import time
import timeout_decorator


def send_json_request(ws, request):
    ws.send(JSON.dumps(request))


def recieve_json_response(ws):
    response = ws.recv()
    if response:
        return JSON.loads(response)

ws = None
wsData = {"CURRENT_URL": None}

connectionsKept = []

class get:
    def __init__(self, wsUrl, identifier=None, timeout=None):
        global ws
        self.Error = False
        if wsUrl != wsData["CURRENT_URL"]:
            wsData["CURRENT_URL"] = wsUrl
            ws = create_connection(wsUrl)

        if identifier != None:
            for identifierKey, identifierValue in identifier.items():
                key = identifierKey
                value = identifierValue

        #@timeout_decorator.timeout(timeout if timeout != 0 else 10**-100) | Removed for now as it causes problems
        def funcWaitForResponse(identifier):
            while True:
                response = ws.recv()
                if response:
                    if identifier != None:
                        if JSON.loads(response)[key] == value:
                            return response
                    else:
                        return response
        self.text = funcWaitForResponse(identifier)

    def json(self):
        return JSON.loads(self.text)

class post:
    def __init__(self, wsUrl, json, identifier=None, timeout=None):
        global ws
        self.Error = False
        if wsUrl != wsData["CURRENT_URL"]:
            wsData["CURRENT_URL"] = wsUrl
            ws = create_connection(wsUrl)

        send_json_request(ws, json)


        #@timeout_decorator.timeout(timeout if timeout != 0 else 10**-100) | Removed for now as it causes problems
        def funcWaitForResponse(identifier):
            while True:
                response = recieve_json_response(ws)
                if response:
                    if identifier != None:
                        for identifierKey, identifierValue in identifier.items():
                            key = identifierKey
                            value = identifierValue
                        if response[key] == value:
                            return response
                    else:
                        return response
        self.text = funcWaitForResponse(identifier)

    def json(self):
        return self.text

def isRunning(wsUrl):
    response = True
    try:
        connectionsKept[wsUrl]
    except Exception:
        response = False

    return response

def heartbeat(wsUrl, interval, payload):
    time.sleep(interval)
    while isRunning(wsUrl):
        heartbeatJSON = payload
        send_json_request(ws, heartbeatJSON)
        time.sleep(interval)

def keepConnection(wsUrl, interval, json):
    connectionsKept.append(wsUrl)
    threading._start_new_thread(heartbeat, (wsUrl, interval, json))

def closeConnection(wsUrl):
    connectionsKept.remove(wsUrl)
    time.cancel()
    ws.close()
