from utils.common_utils import CommonUtility

class SimpleBookApiRequests:
    """
    A class that contains predefined request payloads for the Simple Book API.

    This class includes static attributes that represent the payloads for various operations
    such as obtaining an authentication token, creating an order, and updating an order.
    Each payload is structured as a dictionary to be used directly in API requests.
    """

    AUTH_TOKEN = {
        "clientName": "automation user",
        "clientEmail": f"{CommonUtility.get_unique_email()}",
    }
    """
    Payload for obtaining an authentication token.

    The `AUTH_TOKEN` dictionary includes the following fields:
        - clientName (str): The name of the client requesting authentication.
        - clientEmail (str): A unique email address for the client, generated using
          `CommonUtility.get_unique_email()`.
    """

    CREATE_ORDER = {
        "bookId": 1,
        "customerName": "automation user"
    }
    """
    Payload for creating a new order.

    The `CREATE_ORDER` dictionary includes:
        - bookId (int): The ID of the book to be ordered.
        - customerName (str): The name of the customer placing the order.
    """

    UPDATE_ORDER = {
        "customerName": "automation user updated"
    }
    """
    Payload for updating an existing order.

    The `UPDATE_ORDER` dictionary includes:
        - customerName (str): The updated name of the customer for the order.
    """
