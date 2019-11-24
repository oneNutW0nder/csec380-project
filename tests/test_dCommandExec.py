import requests

#Test case for command execution
def test_CommandExec():
    # Login as valid user -- True
    s = requests.session()
    resp = s.post("https://localhost/login", data={"username": "test_user", "password": "test_password"}, verify=False)

    # Check to see if login was successful by hitting main page
    resp = s.get("https://localhost/", verify=False)
    assert "Videos" in resp.text

    # Send post to /download endpoint with command
    data = {"filename": "testDownload.mp4", "url": "http://techslides.com/demos/sample-videos/small.mp4; echo '<p>comex</p>' >> /app/application/templates/hello.html"}
    resp = s.post("https://localhost/download", data=data, verify=False)
    
    response = requests.get("http://localhost/hello", verify=False)
    assert "comex" in response.text
            
