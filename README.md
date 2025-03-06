# OpenWeather Geolocation Utility

A command-line tool that retrieves **latitude, longitude, and place information** using the [OpenWeather Geocoding API](https://openweathermap.org/api/geocoding-api).<br/>
Supports both city/state and ZIP code queries.

## Features
- Lookup latitude & longitude by city/state or ZIP code
- Handles multiple locations at once  
- Works as a CLI utility for quick lookups  
- Uses OpenWeather API for reliable geolocation  

---

## Prerequisites

Before running the utility or tests, ensure the following dependencies are installed on your system:

- Make sure that Python 3.12.4 is installed on your machine, if not installation instructions are [here](https://www.python.org/downloads/release/python-3124/).
- [Option 1] Make sure you have **pip** installed on your machine. To check it: in terminal run command 
`pip --version`
If not installed follow [these instructions](https://pip.pypa.io/en/stable/installation/).<br/>
  or
- [Option 2] Make sure you have pipenv installed on your machine, check it by running command `pipenv --version`
If not installed, run command `pip install pipenv`. Check again if it's installed by checking its version.

### Set up the project locally and install virtual environment for this project
1. Clone the repo, running command
`git clone https://github.com/risummerit/geoloc-util.git`
2. On your machine go to the project directory for further steps

### In project directory:

**[Option 1]: Install via `pip`**
`pip install -r requirements.txt`

**[Option 2]: Use pipenv Instead**
1. To use pipenv, install dependencies with:
`pipenv install`
2. To activate the virtual environment:
`pipenv shell`
3. This step should be done only once, install virtual environment for this project with python 3.12.4:<br/>
`pipenv --python 3.12.4`
4. Once pipenv is activated, Install all the dependencies from Pipfile:
`pipenv install`

---

## OpenWeather Geolocation utility usage

### Basic CLI Usage
Run the command followed by location names or ZIP codes. Example:

`python geoloc_util.py "Los Angeles, CA" "10001" "Chicago, IL"`

### Example Output
`Location: Los Angeles, State: California, ZIP: N/A (Latitude: 34.0536909, Longitude: -118.242766)`<br/>
`Location: New York, State: New York, ZIP: N/A (Latitude: 40.7127281, Longitude: -74.0060152)`<br/>
`Location: Chicago, State: N/A, ZIP: 60601 (Latitude: 41.8858, Longitude: -87.6181)`

---

## Running tests locally

In this project the tests are written using Pytest framework. Framework documentation: [PyTest documentation](https://docs.pytest.org)

- In your project directory run all tests using command `pytest -vs`
- If you would like to run spesific tests, check pytest.ini file for list of markers (filters), for example: 
Run only end-to-end test:
`pytest -vs -m e2e`
Run only functional tests:
`pytest -vs -m functional`
- Also, you could run file with tests: <br/>
`pytest -vs <\relative path to the file with tests that you would like to run>` <br/>

All tests saved in **test-suite** folder

---

## Running tests with GitHub Actions

Go to GHA page with tests run workflow:
[![Running tests with GitHub Actions](https://github.com/risummerit/geoloc-util/actions/workflows/tests_run.yml/badge.svg)](https://github.com/risummerit/geoloc-util/actions/workflows/tests_run.yml)

Click button "Run workflow" to trigger the tests run. By default 'geoloc_util" marker is selected, it select all tests for OpenWeather Geolocation Utility.<br/>

![image](https://github.com/user-attachments/assets/49421d34-1ccf-42af-a01b-edbcd513bf8b)
Renew the page to see the new workflow running.

---
### Tests reports

Open [allure report](https://risummerit.github.io/geoloc-util/allure-report/) for most recent test run.<br/>
! Make sure to clear browser cache to see new report after each new tests run.
