import requests


def test_helloWorld():
    response = requests.get("http://localhost/hello", verify=False)

    assert "Hello World -- pytesting" in response.text
