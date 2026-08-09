import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    for user in users:
        print("ID:", user["id"])
        print("Name:", user["name"])
        print("Email:", user["email"])
        print()

else:
    print("Unable to get data.")
