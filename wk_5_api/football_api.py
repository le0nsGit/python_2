import requests
import json


def connect_to_api():
    """
    connect_to_api function establishes connection with the openfootball api at Git.
    The function will provide an http code for the connection status.
    # # api response codes: 200: Everything went okay, and the result has been returned (if any). 301: The server is
    # redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name
    # is changed. 400: The server thinks you made a bad request. This can happen when you don’t send along the right
    # data, among other things. 401: The server thinks you’re not authenticated. Many APIs require login credentials,
    # so this happens when you don’t send the right credentials to access an API. 403: The resource you’re trying to
    # access is forbidden: you don’t have the right permissions to see it. 404: The resource you tried to access wasn't’t
    # found on the server. 503: The server is not ready to handle the request.
    Once a connection is made the function will pull table and match date data from the api and output it in a tabular
    format for easy reading.
    """
    # makes a request to api for competition response data
    base_url = 'https://raw.githubusercontent.com'
    endpoint_url = '/openfootball/football.json/master/2020-21/en.1.json'

    # gets requested data from api
    response = requests.get(base_url + endpoint_url)

    # store http return code
    http_code = response.status_code

    # runs depending on returned http response code
    if http_code == 200:
        # prints response data
        print("\n\nYou have connect to the openfootball api....Enjoy\n\n")
        # or
        print(response.text)

    #     # loads json data in list
    #     season_2020 = json.loads(response.text)
    #
    #     #loads inner list into fixtures list
    #     fixtures = season_2020['matches']
    #
    #     #prints title
    #     print("\n\n""2020 - 2021 Premeire League Matches and Dates")
    #     print("-"*82)
    #
    #     #loops through fixtures list and prints matches teams and date of match.
    #     for matches in fixtures:
    #         print(f'{matches["team1"]:<30} {"vs":<10} {matches["team2"]:<30} {matches["date"]}\n')
    #
    # elif http_code == 400:
    #     # prints message user provided bad data
    #     print("You have provided bad data. Cannot connect to api")
    #
    # elif http_code == 401:
    #     # prints message user provided user not authenticated
    #     print("You have not authenticated. Cannot connect to api")
    #
    # elif http_code == 404:
    #     # prints message user cannot find reference
    #     print("Cannot find reference. Cannot connect to api")
    #
    # elif http_code == 500:
    #     # prints message user cannot find reference
    #     print("Server not ready. Cannot connect to api")
    #

# start of main program
if __name__ == "__main__":
    connect_to_api()
