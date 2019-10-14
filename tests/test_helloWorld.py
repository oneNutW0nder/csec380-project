import requests


def test_helloWorld():
    response = requests.get("http://localhost:5000/hello", verify=False)

    assert "Hello World -- pytesting" in response.text
