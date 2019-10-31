import requests


def test_helloWorld():
    response = requests.get("http://127.0.0.1/", verify=False)

    assert "Login" in response.text
