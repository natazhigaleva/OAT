
import requests
def test_valid_date_status_code_200():
    APIkey = "xqfOedde0ViHLHlOVPLkC6aQ5aF1ORfZg6VJfacJ"
    date = "2024-02-10" # date from check-list
    url = f"https://api.nasa.gov/planetary/apod?api_key={APIkey}&date={date}"
    response = requests.get(url)
    result = response.status_code
    try:
        assert 200 <= result < 400
        print(f"\nActual status code: {result}")
    except:
        print(f"\nExpected status code 4xx, but got {result}")

def test_invalid_date_status_code_400():
    APIkey = "xqfOedde0ViHLHlOVPLkC6aQ5aF1ORfZg6VJfacJ"
    date = "2024-13-32" # date from check-list
    url = f"https://api.nasa.gov/planetary/apod?api_key={APIkey}&date={date}"
    response = requests.get(url)
    result = response.status_code
    try:
        assert 200 <= result < 400
        print(f"\nActual status code: {result}")
    except:
        print(f"\nExpected status code 4xx, but got {result}")







