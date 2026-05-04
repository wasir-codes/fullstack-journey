import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)

if response.ok:
    data = response.json()
    print(data)
    print(data["title"])
else:
    print(f"Request failed with status code: {response.status_code}")
