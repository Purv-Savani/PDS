import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("API Data:")
    print(data)
else:
    print("Request failed.")
