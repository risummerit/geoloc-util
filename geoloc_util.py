import argparse
import requests
from config import *


def getInfoByLocations(cityAndState, return_url=False):
    """Fetching latitude and longitude for a city and state."""
    getInfoByLocationsUrl = f"{BASE_URL}/geo/1.0/direct?q={cityAndState},{COUNTRY}&limit=1&appid={TOKEN}"
    url = getInfoByLocationsUrl
    if return_url:
            return url    

    try:
        response = requests.get(getInfoByLocationsUrl)
        response.raise_for_status()  # Raises an HTTPError if the response code is 4xx or 5xx

        data = response.json()
        if data:
            return {
                "name": data[0]["name"],
                "latitude": data[0]["lat"],
                "longitude": data[0]["lon"],
                "state": data[0].get("state", "N/A"),
                "country": data[0]["country"],
                "local_names": data[0]["local_names"]
            }
        return {"error": f"Location '{cityAndState}' not found"}

    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}


def getInfoByZip(zip, return_url=False):
    """Fetching latitude and longitude for a zip code."""
    getInfoByZipUrl = f"{BASE_URL}/geo/1.0/zip?zip={zip},{COUNTRY}&appid={TOKEN}"
    url = getInfoByZipUrl

    if return_url:
            return url  

    try:
        response = requests.get(getInfoByZipUrl)
        response.raise_for_status()  # Raises an HTTPError if the response code is 4xx or 5xx

        if response.status_code == 200:
            data = response.json()
            return {
                "name": data["name"],
                "zip": data["zip"],
                "latitude": data["lat"],
                "longitude": data["lon"],
                "country": data["country"]
            }
        return {"error": f"API request failed with status {response.status_code}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}


def main():
    parser = argparse.ArgumentParser(description="Geolocation Utility using OpenWeather API")
    parser.add_argument("locations", nargs="+", help="List of locations in 'City, State' or ZIP format")

    args = parser.parse_args()
    results = []

    for loc in args.locations:
        if loc.replace(",", "").replace(" ", "").isdigit():
            results.append(getInfoByZip(loc))
        else:
            results.append(getInfoByLocations(loc))

    for res in results:
        if "error" in res:
            print(f"Error: {res['error']}")
        else:
            print(f"Location: {res['name']}, State: {res.get('state', 'N/A')}, zip: {res.get('zip', 'N/A')} (Latitude: {res['latitude']}, Longitude: {res['longitude']})")

if __name__ == "__main__":
    main()
