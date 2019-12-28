import requests

name = input("Enter name :")
email = input("Enter email : ")
mobile = input("Enter mobile : ")
remarks = input("Enter remarks : ")
data = {'name': name, 'email': email, 'mobile': mobile,
        'remarks': remarks}

resp = requests.post("http://localhost:8000/hr/rest/customers/", data)
if resp.status_code == 200:
    print("Customer added successfully!")
else:
    print("Sorry! Could not add Author!")
