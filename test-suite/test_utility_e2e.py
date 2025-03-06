import subprocess
import pytest


"""Ensure CLI runs without errors and returns valid JSON output."""
@pytest.mark.geoloc_util
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.parametrize("cli_args", [
    ["Los Angeles,CA"],
    ["90012"],
    ["Madison,WI"],
    ["10001"]
], ids=[
    "City-State: Los Angeles,CA",
    "ZIP Code: 90012",
    "City-State: Madison,WI",
    "ZIP Code: 10001"
])
def test_smoke_cli_runs_successfully(cli_args):
    
    result = subprocess.run(["python", "geoloc_util.py"] + cli_args, capture_output=True, text=True)
    
    assert result.returncode == 0, f"CLI failed to execute: {result.stderr}"
    assert result.stdout.strip() != "", "CLI returned empty output" 


"""Running the 'geoloc_util' utility using CLI and checking if expected output appears."""
@pytest.mark.geoloc_util
@pytest.mark.e2e
@pytest.mark.parametrize("cli_args, expected_output", [
    (["Los Angeles,CA"], "Los Angeles"),
    (["90012"], "Los Angeles"),
    (["Madison,WI"], "Madison"),
    (["10001"], "New York")
], ids=[
    "City-State: Los Angeles,CA",
    "ZIP Code: 90012",
    "City-State: Madison,WI",
    "ZIP Code: 10001"
])
def test_geolocation_utility_e2e(cli_args, expected_output):
    
    result = subprocess.run(["python", "geoloc_util.py"] + cli_args, capture_output=True, text=True)

    assert result.returncode == 0, f"CLI failed: {result.stderr}"
    assert expected_output in result.stdout, f"Expected '{expected_output}' in output, but got:\n{result.stdout}"
