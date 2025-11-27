import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

def create_user(token, username):
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)

def graph(token, username):
    graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
    graph_params = {
        "id": "graph2",
        "name": "Reading Graph",
        "unit": "Sides",
        "type": "int",
        "color": "ajisai"
    }
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    print(response)

def post_pixel(token, username, graph_id):
    date = datetime.now()
    graph_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
    graph_params = {
        "date": date.strftime("%Y%m%d"),
        "quantity": "100",
    }
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    print(response)

def update_pixel(username, token, graph_id, date):
    graph_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date}"
    graph_params = {
        "quantity": "200",
    }
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.put(url=graph_endpoint, json=graph_params, headers=headers)
    print(response.text)
def delete_pixel(username, token, graph_id, date):
    graph_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date}"
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.delete(url=graph_endpoint, headers=headers)
    print(response.text)
