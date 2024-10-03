import requests

from config.api_config import ApiUrls
from restclient import apiclient
from utils.common_utils import CommonUtility
from utils.requests_payload import SimpleBookApiRequests


class UpdateOrder:
    @staticmethod
    def update_order(order_id):
        """
        Update an order by its ID through the API.

        This method sends a PATCH request to the API endpoint to update the details of an order
        identified by the provided order ID. It handles errors gracefully and logs any issues
        that occur during the request.

        Parameters:
            order_id (str or int): The ID of the order to be updated.

        Returns:
            requests.Response: The response object from the API if the update is successful.
            None: If the update fails due to an HTTP error or any unexpected exceptions.

        Raises:
            requests.exceptions.HTTPError: This is raised if the response status code indicates a failure
            (e.g., 4xx or 5xx errors). The method logs the error and does not raise it further.
        """
        try:
            response = apiclient.patch_request(
                ApiUrls.url_get_order_by_id(order_id),
                None,
                SimpleBookApiRequests.UPDATE_ORDER,
                CommonUtility.get_custom_header()
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response  # Return response if successful
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error while updating order {order_id}: {err}")
        except Exception as e:
            print(f"Unexpected error while updating order {order_id}: {e}")

        return None
