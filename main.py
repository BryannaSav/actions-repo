import os
import requests

def send_mail(message):
    print("Sending mail: " + message)

def test_apis():

    results = ""

    # TS Pet Shelters
    name = "TS Pet Shelters"
    url = "https://api.techsmart.codes/pet-shelter/shelters?name=Kirkland%20Shelter"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()[0]["city"] != "Kirkland":
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
           results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # TS Job Search
    name = "TS Job Search"
    url = "https://api.techsmart.codes/job-search/jobs?title=UX%20Engineer,%20Front%20End"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()[0]["employer"] != "Google":
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
            results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # TS Colors
    name = "TS Colors"
    url = "https://api.techsmart.codes/colors/red"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()["hex"] != "e50000":
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
           results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # TS Anagrams
    name = "TS Anagrams"
    url = "https://api.techsmart.codes/anagrams/words?length=5"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()[0]["longest word"] != "VALUE":
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
           results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # TS Recipes
    name = "TS Recipes"
    url = "https://api.techsmart.codes/nutrition/recipes?name=Drop%20Biscuits%20and%20Sausage%20Gravy"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()[0]["url"] != "http://thepioneerwoman.com/cooking/2013/03/drop-biscuits-and-sausage-gravy/":
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
           results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # TV Maze
    name = "TV Maze"
    url = "https://api.tvmaze.com/search/shows?q=the%20leftovers"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()[0]["show"]["id"] != 138:
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
            results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # The Bored API
    name = "The Bored API"
    url = "https://bored.api.lewagon.com/api/activity?participants=2"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()["participants"] != 2:
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
            results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # Open Trivia DB
    name = "Open Trivia DB"
    url = "https://opentdb.com/api.php?amount=1&category=12&encode=base64"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif len(response.json()["results"][0]["difficulty"]) < 2:
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
            results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # Weather.gov
    name = "Weather.gov"
    url = "https://api.weather.gov/points/47.037872,-122.900696"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()["properties"]["relativeLocation"]["properties"]["city"] != "Olympia":
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
            results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # Data.gov
    name = "Data.gov"
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?api_key=1aaxtpRrtGy47cUMTADVd2rswLmqcpUBbbMqaYT3&school.state=WA&fields=id&sort=id"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()["results"][0]["id"] != 102845:
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
            results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # Free Geo IP
    name = "Free Geo IP"
    url = "https://reallyfreegeoip.org/json/8.8.8.8"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()["country_code"] != "US":
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
            results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # Domains DB
    name = "Domains DB"
    url = "https://api.domainsdb.info/v1/domains/search?domain=google"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif len(response.json()["domains"]) < 2:
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
            results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # Open Library
    name = "Open Library"
    url = "https://openlibrary.org/isbn/9780072435177.json"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()["title"] != "The House on Mango Street":
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
            results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # Random User
    name = "Random User"
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif len(response.json()["results"][0]["name"]["first"]) < 2:
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
            results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    # REST Countries
    name = "REST Countries"
    url = "https://restcountries.com/v3/lang/SWA"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            send_mail("Request to " + name + " (" + url + ") " + " failed with status code " + str(response.status_code))
            results += name + ": <b>Error</b><br><br>"
        elif response.json()[0]["name"]["common"] not in ["Uganda", "DR Congo", "Kenya", "Tanzania"]:
            send_mail("Unexpected response from " + name + " (" + url + ") ")
            results += name + ": <b>Error</b><br><br>"
        else:
            results += name + ": Success<br><br>"
    except:
        send_mail("Unexpected error when testing " + name + " (" + url + ") ")
        results += name + ": <b>Error</b><br><br>"

    return results


if __name__ == "__main__":
    test_apis()
