### Dostęp do API:

```
https://api.aviationstack.com/v1/flights?access_key = YOUR_ACCESS_KEY
```

### Common API Errors:

```markdown
Code Type Description 401 invalid_access_key An invalid API access key was supplied. 401 missing_access_key No API
access key was supplied. 401 inactive_user The given user account is inactive. 403 https_access_restricted HTTPS access
is not supported on the current subscription plan. 403 function_access_restricted The given API endpoint is not
supported on the current subscription plan. 404 invalid_api_function The given API endpoint does not exist. 404
404_not_found Resource not found. 429 usage_limit_reached The given user account has reached its monthly allowed request
volume. 429 rate_limit_reached The given user account has reached the rate limit. 500 internal_error An internal error
occurred.
```

### Optional parameters:

```markdown
access_key    [Required] Your API access key, which can be found in your acccount dashboard. flight_number    [Optional]
Filter your results by providing a flight number. Example: 2557
```

### Sample code:

```python
import requests

params = {
    'access_key': 'YOUR_ACCESS_KEY'
}

api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()

for flight in api_response['results']:
    if (flight['live']['is_ground'] is False):
        print(
            f"{flight['airline']['name']} flight {flight['flight']['iata']} from {flight['departure']['airport']} ({flight['departure']['iata']}) to {flight['arrival']['airport']} ({flight['arrival']['iata']}) is in the air.")
```