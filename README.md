#*Football 2020-21 API*
_______________________

##About:
The Football 2020-21 api will provide current teams and match dates data in a table format.
Data is received via json format from the 
[openfootball](https://github.com/openfootball/football.json/blob/master/2020-21/en.1.json) api at
https://github.com/openfootball/football.json/blob/master/2020-21/en.1.json. This is a free public api that requires
no authentication keys.

##Functions:
The api only consists of one function connect_to_api().
There is no need for the user to enter any data as the table will be run at start. 

###Function Code:

def connect_to_api():

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
        # print(response.text)

        # loads json data in list
        season_2020 = json.loads(response.text)

        #loads inner list into fixtures list
        fixtures = season_2020['matches']

        #prints title
        print("\n\n""2020 - 2021 Premeire League Matches and Dates")
        print("-"*82)

        #loops through fixtures list and prints matches teams and date of match.
        for matches in fixtures:
            print(f'{matches["team1"]:<30} {"vs":<10} {matches["team2"]:<30} {matches["date"]}\n')

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

`# start of main program
if __name__ == "__main__":
    connect_to_api()`



##Results:
Table results will be reflect to your monitor the same as the follwing example and will include
all teams.

![Football 2020-21 Table Results!](wk_5_api/images/results.jpg)

##HTTP Codes:
The Football 202-21 api will provide the following codes when thying to connect or if and issue cocurs while tyring t0
connect:

api response codes: 200: Everything went okay, and the result has been returned (if any). 

301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an
endpoint name is changed.

400: The server thinks you made a bad request. This can happen when you don’t send along the right

data, among other things. 401: The server thinks you’re not authenticated. Many APIs require login credentials,
so this happens when you don’t send the right credentials to access an API. 403: The resource you’re trying to
access is forbidden: you don’t have the right permissions to see it. 404: The resource you tried to access wasn't’t

found on the server. 503: The server is not ready to handle the request.



#####Week
5 Python 2 api's
####Creator:
Leon Boczkowski

####Contact:
lbocz@acd.ccac.edu