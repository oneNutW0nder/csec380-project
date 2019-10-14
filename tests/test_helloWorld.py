import requests


def test_helloWorld():
    response = requests.get("http://localhost:80/", verify=False)

    assert "Login" in response.text
