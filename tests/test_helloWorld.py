import requests


def test_helloWorld():
    response = requests.get("https://localhost:8080/hello.html", verify=False)

    assert "Hello World -- pytesting" in response.text
