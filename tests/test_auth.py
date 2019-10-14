import requests


def valid_login():
    """
    test a valid login
    """
    resp = requests.post("https://localhost/login", data={"username": "test_user", "password": "test_password"}, verify=False)

    if "Welcome" in resp.text:
        return True
    else:
        return False


def bad_userlogin():
    """
    test a bad login with only bad username
    """
    resp = requests.post("https://localhost/login", data={"username": "adfs", "password": "test_password"}, verify=False)

    if "Invalid" in resp.text:
        return True
    else:
        return False


def bad_passlogin():
    """
    test a bad login with only bad password
    """
    resp = requests.post("https://localhost/login", data={"username": "test_user", "password": "test_password"}, verify=False)

    if "Invalid" in resp.text:
        return True
    else:
        return False


def test_run_all():
    """
    run all the tests for this section
    """
    assert valid_login()
    assert bad_userlogin()
    assert bad_passlogin()
