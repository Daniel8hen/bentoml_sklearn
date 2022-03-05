import requests

resp = requests.post(
    "http://127.0.0.1:5000/classify",
    headers={"content-type": "application/json"},
    data="[1238912389123,-565,123,1]").text

print(resp)