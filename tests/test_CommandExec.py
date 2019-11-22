import requests

def test_CommandExec():
    # Login as valid user -- True
    s = requests.session()
    resp = s.post("https://localhost/login", data={"username": "test_user", "password": "test_password"}, verify=False)

    # Check to see if login was successful by hitting main page
    resp = s.get("https://localhost/", verify=False)
    assert "Videos" in resp.text

    # Send post to /download endpoint
    data = {"filename": "testDownload.mp4", "url": "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4; [command]"}
    resp = s.post("https://localhost/download", data=data, verify=False)
    assert "successfully" in resp.text
    
    #To-Do: Write test case for command execution
