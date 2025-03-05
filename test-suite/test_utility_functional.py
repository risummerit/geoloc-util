import pytest
from config import *
from geoloc_util import *
from data_for_tests import *


"""Testing the health of URLs."""
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.parametrize("url", 
                        [
                            BASE_URL,
                            getInfoByLocations(cityAndStateTestData, return_url=True),
                            getInfoByZip(zipTestData, return_url=True)
                        ],
                        ids=
                        [  # Custom test names (IDs) to prevent printing the full URL with tokens in the test report.
                            "BASE_URL",
                            "Location Geocode API",
                            "ZIP Code Geocode API",
                        ]
                        )
def test_smoke_urls_healthy(url):

    response = requests.get(url)
    assert response.status_code == 200, f"Smoke test failed - can not to get {url}"


"""Testing the `getInfoByLocations` function with different location test data."""
@pytest.mark.functional
@pytest.mark.parametrize("locationTest", [cityAndStateTestData, cityAndStateTestData2])
def test_get_info_by_location(locationTest):

    data = getInfoByLocations(locationTest) 

    assert "name" in data
    assert "latitude" in data or "lat" in data
    assert "longitude" in data or "lon" in data
    assert "country" in data
    assert "state" in data
    assert "local_names" in data

    if locationTest == "Los Angeles, CA":
        assert data["name"] == "Los Angeles"
        assert data["country"] == "US"
        assert data["state"] == "California"
        assert (data["latitude"] if "latitude" in data else data["lat"]) == 34.0536909
        assert (data["longitude"] if "longitude" in data else data["lon"]) == -118.242766
        assert data["local_names"]["en"] == "Los Angeles"

    elif locationTest == "Madison, WI":
        assert data["name"] == "Madison"
        assert data["country"] == "US"
        assert data["state"] == "Wisconsin"
        assert (data["latitude"] if "latitude" in data else data["lat"])  == 43.074761
        assert (data["longitude"] if "longitude" in data else data["lon"]) == -89.3837613
        assert data["local_names"]["en"] == "Madison"


"""Testing the `getInfoByZip` function using parameterized zip code test data."""
@pytest.mark.functional
@pytest.mark.parametrize("zipCodeTest", [zipTestData, zipTestData2])
def test_get_info_by_zip(zipCodeTest):

    data = getInfoByZip(zipCodeTest)

    assert "zip" in data
    assert "name" in data
    assert "latitude" in data or "lat" in data
    assert "longitude" in data or "lon" in data
    assert "country" in data

    if zipCodeTest == "90012":
        assert data["zip"] == "90012"
        assert data["name"] == "Los Angeles"
        assert (data["latitude"] if "latitude" in data else data["lat"]) == 34.0614
        assert (data["longitude"] if "longitude" in data else data["lon"]) == -118.2385
        assert data["country"] == "US"
    
    elif zipCodeTest == "12345":
        assert data["zip"] == "12345"
        assert data["name"] == "Schenectady"
        assert (data["latitude"] if "latitude" in data else data["lat"]) == 42.8142
        assert (data["longitude"] if "longitude" in data else data["lon"]) == -73.9396
        assert data["country"] == "US"


"""Verifying that API requests without a token return a 401 status code."""
@pytest.mark.functional
@pytest.mark.functional_negative
@pytest.mark.parametrize("api_function, input_value", [
    (getInfoByLocations, "Los Angeles,CA"),
    (getInfoByZip, "90012")
])
def test_negative_no_token(api_function, input_value):
    url = api_function(input_value, return_url=True).replace(TOKEN, "")
    response = requests.get(url)
    assert response.status_code == 401, f"Negative test failed - {url} without a token should return 401"


"""Verifying that API requests with invalid token return a 401 status code."""
@pytest.mark.functional
@pytest.mark.functional_negative
@pytest.mark.parametrize("api_function, input_value", [
    (getInfoByLocations, "Los Angeles,CA"),
    (getInfoByZip, "90012")
])
def test_negative_invalid_token(api_function, input_value):
    url = api_function(input_value, return_url=True).replace(TOKEN, "Invalid")
    response = requests.get(url)
    assert response.status_code == 401, f"Negative test failed - {url} with invalid token should return 401"


"""Verifying that API requests with iinvalid data in requests return a 404 status code."""
@pytest.mark.functional
@pytest.mark.functional_negative
@pytest.mark.parametrize("api_function, input_value", [
    (getInfoByLocations, "Los Angeles,CA"),
    (getInfoByZip, "90012")
])
def test_negative_invalid_request_data(api_function, input_value):

    url = api_function(input_value, return_url=True)

    if api_function == getInfoByLocations:
        urlTest = url.replace("q=Los Angeles,CA", "q=")
    if api_function == getInfoByZip:
        urlTest = url.replace("zip=90012", "zip=INVALID")

    response = requests.get(urlTest)
    assert response.status_code == 404, f"Negative test failed - {urlTest} with invalid data in request should return 404"
