import requests

def test_fileupload():
    # Login as valid user -- True
    s = requests.session()
    resp = s.post("https://localhost/login", data={"username": "test_user", "password": "test_password"}, verify=False)

    # Check to see if login was successful by hitting main page
    resp = s.get("https://localhost/", verify=False)
    assert "Videos" in resp.text

    # Post request to /upload endpoint -- True
    files = {"file": open("./tests/videos/small.mp4", "rb")}
    resp = s.post("https://localhost/upload", files=files, verify=False)
    assert "successfully" in resp.text

    # Request to acess the video -- True
    resp = s.get("https://localhost/playback/2", verify=False)
    assert "Delete Video" in resp.text

    # Delete their video -- True
    resp = s.post("https://localhost/playback/2", verify=False)
    assert "video has been deleted" in resp.text

def test_download():
    # Login as valid user -- True
    s = requests.session()
    resp = s.post("https://localhost/login", data={"username": "test_user", "password": "test_password"}, verify=False)

    # Check to see if login was successful by hitting main page
    resp = s.get("https://localhost/", verify=False)
    assert "Videos" in resp.text

    # Send post to /download endpoint
    data = {"filename": "testDownload.mp4", "url": "http://techslides.com/demos/sample-videos/small.mp4"}
    resp = s.post("https://localhost/download", data=data, verify=False)
    assert "successfully" in resp.text

    # Access the video
    resp = s.get("https://localhost/playback/3", verify=False)
    assert "Delete Video" in resp.text

    # Delete their video -- True
    resp = s.post("https://localhost/playback/3", verify=False)
    assert "video has been deleted" in resp.text
