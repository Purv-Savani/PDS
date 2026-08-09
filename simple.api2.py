import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print("URL:", response.url)

if response.status_code == 200:
    data = response.json()

    for post in data[:5]:
        print("ID:", post["id"])
        print("Title:", post["title"])
        print()
else:
    print("Request failed.")
