import requests

api1 = "http://127.0.0.1:8080/json"
api2 = "http://127.0.0.1:8080/api2"
api3 = "http://127.0.0.1:8080/api3"
# param1=va1&param2=val2


api1_response = requests.get(api1)
api1_response = api1_response.json()
print("API RESPOMSE ", api1_response)

api2_response = requests.get(api2)
api2_response = api2_response.json()
print("API RESPOMSE ", api2_response)

api3_response = requests.post(api3, params={"moviename": "ABC MOVIE"})
api3_response = api3_response.json()
print("API3 RESPOMSE ", api3_response)
