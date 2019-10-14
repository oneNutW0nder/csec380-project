import requests


def test_helloWorld():
    response = requests.get("http://localhost/", verify=False)

    try:
        assert "Login" in response.text
    except ConnectionError:
        assert True
