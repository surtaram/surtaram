import requests

from config.api_config import ApiUrls
from conftest import logger
from restclient import apiclient
from utils.common_utils import CommonUtility
from utils.requests_payload import SimpleBookApiRequests


class CreateOrder:
    @staticmethod
    def create_order():
        """
        Create a new order through the API.

        This method sends a POST request to the API endpoint to create a new order.
        It handles errors gracefully and logs any issues that occur during the request.

        Returns:
            requests.Response: The response object from the API if the order is created successfully.
            None: If the order creation fails due to an HTTP error or any unexpected exceptions.

        Raises:
            requests.exceptions.HTTPError: This is raised if the response status code indicates a failure
            (e.g., 4xx or 5xx errors). The method logs the error and does not raise it further.
        """
        try:
            response = apiclient.post_request(
                ApiUrls.url_get_all_orders(),
                None,
                SimpleBookApiRequests.CREATE_ORDER,
                CommonUtility.get_custom_header()
            )
            response.raise_for_status()  # Raises an error for bad responses
            return response  # Return response if successful
        except requests.exceptions.HTTPError as err:
            logger.error(f"HTTP error while creating order: {err}")
        except Exception as e:
            logger.error(f"Unexpected error while creating order: {e}")

        return None
