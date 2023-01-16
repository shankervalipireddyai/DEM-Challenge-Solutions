import requests


url_lambda = "https://kx87oq3ou5.execute-api.us-west-1.amazonaws.com/apitest/predict"
data1 = {"values": [[0.1, 4.8, 3.1, 3]]}
data2 = {"values": [[5.3, 4.0, 3.1, 2.3]]}
result1, result2 = requests.post(url_lambda, json=data1).json(), requests.post(url_lambda, json=data2).json()
print(result1, result2)
