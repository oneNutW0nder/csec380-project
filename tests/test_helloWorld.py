import requests


def test_helloWorld():
    response = requests.get("http://localhost/hello", verify=False)
    print(response.text)
    assert "Hello World -- pytesting" in response.text
