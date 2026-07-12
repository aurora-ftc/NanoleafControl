import requests

class Nanoleaf:
    def __init__(self, ip, token):
        self.url = f"http://{ip}:16021/api/v1/{token}/state"

    def on(self): 
        payload = {
            "on": {
                "value": True
            }
        }

        response = requests.put(self.url, json=payload)

        print(response.status_code)
        print(response.text)       

    def off(self):
        payload = {
            "on": {
                "value": False
            }
        }

        response = requests.put(self.url, json=payload)

        print(response.status_code)
        print(response.text)