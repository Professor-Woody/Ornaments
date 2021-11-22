import time

import json
import network
import urequests as requests

class Wifi:
    wlan = None
    SSID = "OrnamentNet"
    PASSWORD = "ornaments"
    URL = "http://192.168.4.1"

    def __init__(self):
        # Initialize wlan object
        self.wlan = network.WLAN(network.STA_IF)
        if not self.wlan.active():
            self.wlan.active(True)
        ap = network.WLAN(network.AP_IF)
        if ap.active():
            ap.active(False)

        # try to connect to the set wifi AP
        self.wlan.connect(self.SSID, self.PASSWORD)

        # Keep looping until connection is successful
        while True:
            if self.wlan.isconnected():
                print("Connected to: " + self.SSID)
                return
            else:
                time.sleep_ms(500)
                print("Connecting...")

    def sendRequest(self, message):
        response = requests.get(self.URL+ message)
        print(self.URL+ message)
        text = response.text
        print(text)
        response.close()
        return(text)

    def getProgram(self):
        response = self.sendRequest("/getProgram")
        print(response)
        return json.loads(response)