import requests

def test_version_endpoint():
    response = requests.get("http://localhost:5000/version")
    assert response.status_code == 200
    assert response.text == "" 

if __name__ == "__main__":
    test_version_endpoint()
    print("Version endpoint test passed!")
