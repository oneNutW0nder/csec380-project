import requests

@pytest.mark.last
def test_upload():
    # Login as valid user -- True
    s = requests.session()
    resp = s.post("https://localhost/login", data={"username": "test_user", "password": "test_password"}, verify=False)

    # Check to see if login was successful by hitting main page
    resp = s.get("https://localhost/", verify=False)
    assert "Videos" in resp.text

    # Post request to /upload endpoint -- True
    files = {"file": open("./videos/small.mp4", "rb")}
    resp = s.post("https://localhost/upload", files=files, verify=False)
    assert "successfully" in resp.text

    # Request to acess the video -- True
    resp = s.get("https://localhost/playback/1", verify=False)
    assert "Delete Video" in resp.text
    print(resp.text)


    # Delete their video -- True
    resp = s.post("https://localhost/playback/1", verify=False)
    assert "video has been deleted" in resp.text