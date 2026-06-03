# Fakes : When we can build a simple im-memory replacement.
# Mocks : When we just want to verify the call happened. 

## Mocking 

import requests 

def get_weather(city):
    response = requests.get(f"URL/weather/{city}")
    return response.json()

# The above with Mocking 
from unittest.mock import patch

@patch("requests.get")
def test_weather(mock_get):
    mock_get.return_value.json.return_value = {
        "temp" : 20
    } 

    result2 = get_weather("London")
    print(result2)
    assert result2["temp"] == 20

test_weather()