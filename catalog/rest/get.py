import requests

id = input("Enter author id :")
resp = requests.get(f"http://localhost:8000/hr/rest/authors/{id}")
if resp.status_code == 200:
    author = resp.json()
    print(author['name'], author['email'])
else:
    print("Sorry! Author not found!")
