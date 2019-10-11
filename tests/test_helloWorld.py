import requests


def test_helloWorld():
    response = requests.get("http://localhost:8080/hello.html")

    assert "Hello World -- pytesting" in response.text
