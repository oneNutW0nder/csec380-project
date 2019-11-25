import requests


def test_sql_blind_statement():
    """
    test a true condition for an SQL attack
    """
    resp = requests.post("https://localhost/login", data={"username": "'", "password": ""}, verify=False)

    if "ProgrammingError" in resp.text:
        assert True
    else:
        assert False
