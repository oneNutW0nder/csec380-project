import requests


def true_sql_statement():
    """
    test a true condition for an SQL attack
    """
    resp = requests.post("https://localhost/login", data={"username": "' or '1'='1", "password": ""}, verify=False)

    if "Error" in resp.text:
        return True
    else:
        return False


def false_sql_statement():
    """
    test a false condition for an SQL attack
    """
    resp = requests.post("https://localhost/login", data={"username": "' or '1'='2", "password": ""}, verify=False)

    if "Invalid" in resp.text:
        return True
    else:
        return False
