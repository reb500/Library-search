import requests


class FetchError(Exception):
    """A request failed or returned invalid JSON."""


def fetch_data(title=None, author=None, subject=None):
    url = "https://openlibrary.org/search.json"
    params = {
        "title": title,
        "author": author,
        "subject": subject,
    }
    filtered_params = {}

    for key, value in params.items():
        if value is None:
            continue

        if not isinstance(value, str):
            raise ValueError("Search values must be text.")

        value = value.strip()

        if value:
            filtered_params[key] = value
    if not filtered_params:
        raise ValueError("At least one search parameter must be provided.")
    filtered_params["limit"] = 10
    filtered_params["fields"] = "title,author_name,first_publish_year,subject,key"
    try:
        response = requests.get(url, params=filtered_params, timeout=10)
        response.raise_for_status()

        data = response.json()

        return data
    except requests.exceptions.Timeout as error:
        raise FetchError("Request timed out. Please try again.") from error
    except requests.exceptions.ConnectionError as error:
        raise FetchError("Could not connect to the API.") from error
    except requests.exceptions.JSONDecodeError as error:
        raise FetchError("The response is not valid JSON.") from error
    except requests.exceptions.RequestException as error:
        raise FetchError(f"Request error: {error}") from error
