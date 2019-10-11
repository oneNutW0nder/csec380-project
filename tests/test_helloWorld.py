import requests


def test_helloWorld():
    response = requests.get("https://localhost/hello.html", verify=False)

    assert "Hello World -- pytesting" in response.text
