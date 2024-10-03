from restclient import apiclient

class ApiUrls:
    """
    A class that provides endpoints for the API related to orders and authentication.

    This class contains static methods that return the URLs for various API operations
    such as authentication, retrieving all orders, and fetching orders by their ID.
    """

    @staticmethod
    def url_get_auth():
        """
        Get the authentication endpoint URL.

        Returns:
            str: The URL for the authentication endpoint.
        """
        return apiclient.get_base_end_point() + "/api-clients/"

    @staticmethod
    def url_get_all_orders():
        """
        Get the URL for retrieving all orders.

        Returns:
            str: The URL for the endpoint to fetch all orders.
        """
        return apiclient.get_base_end_point() + "/orders"

    @staticmethod
    def url_get_order_by_id(order_id):
        """
        Get the URL for retrieving an order by its ID.

        Parameters:
            order_id (str or int): The ID of the order to be fetched.

        Returns:
            str: The URL for the endpoint to fetch a specific order by ID.
        """
        return apiclient.get_base_end_point() + f"/orders/{order_id}"
