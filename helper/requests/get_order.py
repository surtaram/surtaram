import requests

from config.api_config import ApiUrls
from conftest import logger
from restclient import apiclient
from utils.common_utils import CommonUtility


class GetOrder:
    @staticmethod
    def get_order_by_id(order_id):
        """
        Retrieve an order by its ID through the API.

        This method sends a GET request to the API endpoint to fetch the details of an order
        identified by the provided order ID. It handles errors gracefully and logs any issues
        that occur during the request.

        Parameters:
            order_id (str or int): The ID of the order to be retrieved.

        Returns:
            requests.Response: The response object containing the order details if the retrieval is
            successful.
            None: If the retrieval fails due to an HTTP error or any unexpected exceptions.

        Raises:
            requests.exceptions.HTTPError: This is raised if the response status code indicates a failure
            (e.g., 4xx or 5xx errors). The method logs the error and does not raise it further.
        """
        try:
            response = apiclient.get_request(
                ApiUrls.url_get_order_by_id(order_id),
                None,
                CommonUtility.get_custom_header()
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response  # Return response if successful
        except requests.exceptions.HTTPError as err:
            logger.error(f"HTTP error while retrieving order {order_id}: {err}")
        except Exception as e:
            logger.error(f"Unexpected error while retrieving order {order_id}: {e}")

        return None  # Return None on failure
