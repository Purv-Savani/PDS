import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python Data Science",
    "body": "Learning API with Python",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())
