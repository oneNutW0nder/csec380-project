import requests


def test_helloWorld():
    response = requests.get("http://localhost", verify=False)

    assert "Login" in response.text
