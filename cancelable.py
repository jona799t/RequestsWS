import time as TIME

shouldCancelSleep = False

class time:
    def sleep(seconds):
        global shouldCancelSleep
        shouldCancelSleep = False

        endSleep = TIME.time() + seconds
        while True:
            if shouldCancelSleep:
                break
            if TIME.time() >= endSleep:
                break

    def cancel():
        global shouldCancelSleep
        shouldCancelSleep = True

class input:
    def __init__(self, question):
        print(question)
        print("Not supported yet")
