import requests
import json


# # api response codes: 200: Everything went okay, and the result has been returned (if any). 301: The server is
# redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name
# is changed. 400: The server thinks you made a bad request. This can happen when you don’t send along the right
# data, among other things. 401: The server thinks you’re not authenticated. Many APIs require login credentials,
# so this happens when you don’t send the right credentials to access an API. 403: The resource you’re trying to
# access is forbidden: you don’t have the right permissions to see it. 404: The resource you tried to access wasn't’t
# found on the server. 503: The server is not ready to handle the request.

def connect_to_api():
    # makes a request to api for competition response data
    base_url = 'https://raw.githubusercontent.com'
    endpoint_url = '/openfootball/football.json/master/2020-21/en.1.json'

    # gets requested data from api
    response = requests.get(base_url + endpoint_url)

    # converts json data to python dictionary data and stores in var
    # premiere_league = response.json()

    # store http return code
    http_code = response.status_code

    # runs depending on returned http response code
    if http_code == 200:
        # prints response data
        # print(premiere_league)
        # or
        print(response.text)

    elif http_code == 400:
        # prints message user provided bad data
        print("You have provided bad data. Cannot connect to api")

    elif http_code == 401:
        # prints message user provided user not authenticated
        print("You have not authenticated. Cannot connect to api")

    elif http_code == 404:
        # prints message user cannot find reference
        print("Cannot find reference. Cannot connect to api")

    elif http_code == 500:
        # prints message user cannot find reference
        print("Server not ready. Cannot connect to api")


# start of main program
if __name__ == "__main__":
    connect_to_api()
