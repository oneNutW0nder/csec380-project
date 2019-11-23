import requests

#Test case for command execution
def test_CommandExec():
    #Create User
    resp = requests.post("https://localhost/register", data={"username": "test_exec", "password": "exec_password", "confirmpassword": "exec_password"}, verify=False)
    
    # Login as valid user -- True
    s = requests.session()
    resp = s.post("https://localhost/login", data={"username": "test_exec", "password": "exec_password"}, verify=False)

    # Check to see if login was successful by hitting main page
    resp = s.get("https://localhost/", verify=False)
    assert "Videos" in resp.text

    # Send post to /download endpoint with command
    data = {"filename": "testDownload.mp4", "url": "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4; echo '<p>comex</p>' >> hello.html"}
    resp = s.post("https://localhost/download", data=data, verify=False)
    
    response = requests.get("http://localhost", verify=False)
    assert "comex" in response.text
            
