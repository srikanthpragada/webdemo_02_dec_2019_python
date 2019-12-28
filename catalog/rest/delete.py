import requests

id = input("Enter customer id :")
resp = requests.delete(f"http://localhost:8000/hr/rest/customers/{id}")
if resp.status_code == 204:
    print("Customer was deleted successfully!")
else:
    print("Sorry! Customer not found!")
