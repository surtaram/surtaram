import json
import requests


def get_base_end_point():
    """
    Retrieve the base URL from the JSON configuration file based on the specified environment.

    :return: Base URL of the specified environment.
    :raises FileNotFoundError: If the endpoints.json file is not found.
    :raises KeyError: If the environment or base URL is not defined in the JSON.
    """
    # Load the configuration from the JSON file
    with open("config/endpoints.json") as json_file:
        properties = json.load(json_file)

        # Get the current environment
        env = properties["environment"]["env"]

        # Return the base URL for the environment
        return properties[env]["base_url"]


def get_request(url, params=None, headers=None):
    """
    Perform a GET request.

    :param url: The URL to send the GET request to.
    :param params: Optional dictionary of query parameters to include in the request.
    :param headers: Optional dictionary of HTTP headers to include in the request.
    :return: Response object from the requests library.
    """
    # Send the GET request and raise an error for bad responses
    response = requests.get(url=url, params=params, headers=headers)
    response.raise_for_status()  # Raises an error for 4xx/5xx responses
    return response


def post_request(url, params=None, json=None, headers=None):
    """
    Perform a POST request.

    :param url: The URL to send the POST request to.
    :param params: Optional dictionary of query parameters to include in the request.
    :param json: The JSON data to send in the body of the request.
    :param headers: Optional dictionary of HTTP headers to include in the request.
    :return: Response object from the requests library.
    """
    # Send the POST request and raise an error for bad responses
    response = requests.post(url=url, params=params, json=json, headers=headers)
    response.raise_for_status()  # Raises an error for 4xx/5xx responses
    return response


def put_request(url, params=None, json=None, headers=None):
    """
    Perform a PUT request.

    :param url: The URL to send the PUT request to.
    :param params: Optional dictionary of query parameters to include in the request.
    :param json: The JSON data to send in the body of the request.
    :param headers: Optional dictionary of HTTP headers to include in the request.
    :return: Response object from the requests library.
    """
    # Send the PUT request and raise an error for bad responses
    response = requests.put(url=url, params=params, json=json, headers=headers)
    response.raise_for_status()  # Raises an error for 4xx/5xx responses
    return response


def patch_request(url, params=None, json=None, headers=None):
    """
    Perform a PATCH request.

    :param url: The URL to send the PATCH request to.
    :param params: Optional dictionary of query parameters to include in the request.
    :param json: The JSON data to send in the body of the request.
    :param headers: Optional dictionary of HTTP headers to include in the request.
    :return: Response object from the requests library.
    """
    # Send the PATCH request and raise an error for bad responses
    response = requests.patch(url=url, params=params, json=json, headers=headers)
    response.raise_for_status()  # Raises an error for 4xx/5xx responses
    return response


def delete_request(url, params=None, headers=None):
    """
    Perform a DELETE request.

    :param url: The URL to send the DELETE request to.
    :param params: Optional dictionary of query parameters to include in the request.
    :param headers: Optional dictionary of HTTP headers to include in the request.
    :return: Response object from the requests library or JSON response if content is available.
    """
    # Send the DELETE request and raise an error for bad responses
    response = requests.delete(url=url, params=params, headers=headers)
    response.raise_for_status()  # Raises an error for 4xx/5xx responses

    # Return JSON data if the response contains content; otherwise, return an empty dict
    return response.json() if response.content else response