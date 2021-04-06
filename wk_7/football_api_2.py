import requests
import json
import pandas as pd

base_url = "https://api-football-v1.p.rapidapi.com/v2"

querystring = {"timezone": "Europe/London"}

key = ''

# gets api key from json file
with open('dont_push/key.json', 'r') as api_key:
    key = json.load(api_key)
    print(key)

headers = {
    'x-rapidapi-key': key['api_key'],
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
}


def status(http_code):
    """
    will output message and code upon if status being met
    Args:
        http_code: store http return code

    Returns: none

    """
    # store http return code
    # http_code = response.status_code

    # runs depending on returned http response code
    if http_code == 200:
        # prints response data
        print("\n\nYou have connect to the openfootball api....Enjoy\n\n")
        # or
        print(f"Output Code: {http_code}")

    elif http_code == 400:
        # prints message user provided bad data
        print("You have provided bad data. Cannot connect to api")
        print(f"Output Code: {http_code}")

    elif http_code == 401:
        # prints message user provided user not authenticated
        print("You have not authenticated. Cannot connect to api")
        print(f"Output Code: {http_code}")

    elif http_code == 404:
        # prints message user cannot find reference
        print("Cannot find reference. Cannot connect to api")
        print(f"Output Code: {http_code}")

    elif http_code == 500:
        # prints message user cannot find reference
        print("Server not ready. Cannot connect to api")
        print(f"Output Code: {http_code}")


def teams(base_url, endpoint="/teams/league/2790"):
    """
    connects to football api and stores data in list.
    gets response data
    loops through the list of dictionary text from response data and adds that data to prem_league list
    outputs prem league list data in pandas table using pre determined format.
    if execption raised will print error message

    Args:
        base_url: the base url to connect to api main
        endpoint: the teams data at api

    Returns:none

    """
    # appends endpoint to base url
    url = base_url + endpoint

    try:
        # gets requested data from api and stores in var
        response = requests.get(url, headers=headers, params=querystring)

        # store http return code status
        # response.status_code

        # runs status code function
        status(response.status_code)

        # appends data from api to football teams dictionary
        football_teams_d = json.loads(response.text)

        # print(type(football_teams_d))
        prem_team_l = []

        # # loops through football_teams_d and appends team data to prem_team_l using list comprehesion
        prem_team_l = [t for t in football_teams_d['api']['teams']]

        # for x in prem_team_l:
        #     print(json.dumps(x,indent=1))

        run_as_dataframe(prem_team_l=prem_team_l)

    except Exception as e:
        print(f'You have the following errors in code: {e}')


def run_as_dataframe(prem_team_l):
    """
    Accepts premeire league table data and outputs as a Pandas table using its dataframe functions.

    Args:
        prem_team_l:

    Returns:

    """
    # sets up
    df = pd.DataFrame(data=prem_team_l,
                      columns=['team_id', 'name', 'founded', 'venue_name', 'venue_city', 'venue_capacity'])

    # prints team information as pandas tables
    print(df.head(20))


def main():
    print("\n\nWelcome to the Premiere League API!\nHere we will provide you with current football teams"
          "data happening in the league, including current match data and scores!\n\n")

    # endpoints_d = {'teams': teams}
    # #
    # # endpoints_d.get('teams')()

    # runs team function
    teams(base_url)


if __name__ == '__main__':
    main()
