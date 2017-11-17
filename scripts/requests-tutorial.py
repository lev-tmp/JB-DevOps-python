# Requests: HTTP for Humans
# http://docs.python-requests.org/en/master/
####
# HTTP in nutshell:
# Two commonly used methods for a request-response between a client and server are: GET and POST.
# GET - Requests data from a specified resource
# POST - Submits data to be processed to a specified resource
# https://www.w3schools.com/tags/ref_httpmethods.asp
# List of HTTP status codes : https://www.w3schools.com/tags/ref_httpmessages.asp
# Let's example with some NASA open API and requests python module
# http://api.open-notify.org example for API , we will see only GET request examples. For POST continue explore by yourself.

import requests

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)
print(response.text)

# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
print(data["number"])
print(data)
