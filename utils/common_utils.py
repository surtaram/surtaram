import logging
import random
import os
from dotenv import load_dotenv, dotenv_values

# Load environment variables from the .env file
load_dotenv()

class CommonUtility:
    """
    A utility class providing common functions for the application.

    This class includes methods for generating custom headers and creating unique email addresses.
    It retrieves the authorization token from environment variables and ensures that the headers
    required for API requests are correctly formatted.
    """

    @staticmethod
    def get_custom_header():
        """
        Retrieve custom headers for API requests.

        This method fetches the authorization token from environment variables
        and constructs the headers necessary for making API requests.

        Returns:
            dict: A dictionary containing the 'Authorization' and 'Content-Type' headers.
        """
        bearer_token = os.getenv("AUTH_TOKEN")
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }
        return headers

    @staticmethod
    def get_unique_email():
        """
        Generate a unique email address for testing purposes.

        This method creates an email address by appending a random number to a fixed string,
        ensuring that the email is unique each time it is called.

        Returns:
            str: A unique email address in the format 'test_automation{random_number}@gmail.com'.
        """
        random_number = random.randint(1000, 99999)
        email = f"test_automation{random_number}@gmail.com"
        return email
