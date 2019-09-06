import requests


def test_helloWorld():
    response = requests.get("http://localhost:80")

    assert "Hello World -- pytesting" in response.text
