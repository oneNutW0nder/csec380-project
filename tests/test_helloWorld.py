import requests


def test_helloWorld():
    response = requests.get("http://localhost:8080", verify=false)

    assert "Hello World -- pytesting" in response.text
