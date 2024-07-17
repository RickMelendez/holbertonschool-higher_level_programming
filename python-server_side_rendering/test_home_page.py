import requests

def test_home_page():
    response = requests.get('http://127.0.0.1:5000')
    assert response.status_code == 200, "Failed: Home page did not load"
    content = response.text
    assert '<header>' in content, "Failed: Header not found in Home page"

if __name__ == "__main__":
    test_home_page()
    print("All tests passed!")
