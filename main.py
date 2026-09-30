import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "srithika"
TOKEN = "asdfasdfasdf"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

book_name = str(input("What book did you read today? "))
author_name = str(input("Who is the author? "))
pages = int(input("How many pages did you read? "))

graph = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : "graph1",
    "name" : "Reading Tracker",
    "unit" : "Pages",
    "type" : "int",
    "color" : "shibafu",
}
headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph, json=graph_config, headers=headers)
# print(response.text)
day = datetime.now().strftime("%Y%m%d")
pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_config = {
    "date" : day,
    "quantity" : "12",
    "optionalData" :  f'{{"Book": "{book_name}", "Author": "{author_name}"}}'
}
response = requests.post(url=pixel, json=pixel_config, headers=headers)
 
change_endpoint = f"{pixel}/{day}"
update_config = {
    "quantity" : pages,
}
# response = requests.put(url=change_endpoint, json=update_config, headers=headers)
# print(response.text)

# response = requests.delete(url=change_endpoint, headers=headers)
# print(response.text)
