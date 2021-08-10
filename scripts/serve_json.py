import json
import requests

def serveJson():
    URL = "http://127.0.0.1:5000/colors"
    f = open('colors.json')
    data = json.load(f)
    for color in data:
        requests.post(URL, json=color)

if __name__ == "__main__":
    serveJson()