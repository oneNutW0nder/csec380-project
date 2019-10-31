import requests


def test_helloWorld():
    response = requests.get("https://localhost/", verify=False)

    assert "Login" in response.text
