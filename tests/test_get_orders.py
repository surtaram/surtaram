import pytest
import allure

from conftest import logger
from helper.requests.create_order import CreateOrder
from helper.requests.get_order import GetOrder


@allure.epic("Retrieve an order")
@allure.feature("Get Order Feature")
class TestGetBook:

    @pytest.mark.order(1)
    @allure.story("Retrieve an order by ID")
    @allure.title("Test Get Order By ID")
    @allure.description("Test to create a new order and then retrieve it by ID to verify its details.")
    def test_get_order_by_id(self):
        """
        Test to create a new order and then retrieve it by ID to verify its details.
        """
        # Create a new order and handle any errors
        post_response = CreateOrder.create_order()
        if post_response is None:
            logger.error("Failed to create a new order.")
            pytest.fail("Failed to create a new order.")

        order_id = post_response.json().get('orderId')  # Safely access orderId
        logger.info(f"New order created with ID: {order_id}")

        # Get the order by ID and handle any errors
        get_response = GetOrder.get_order_by_id(order_id)
        if get_response is None:
            logger.error(f"Failed to retrieve order with ID: {order_id}")
            pytest.fail(f"Failed to retrieve order with ID: {order_id}")

        # Assertions to verify the order details
        assert get_response.json().get('bookId') == 1, (
            f"Expected 'bookId' to be 1 but got {get_response.json().get('bookId')}"
        )
        assert get_response.json().get('customerName') == 'automation user', (
            f"Expected 'customerName' to be 'automation user' but got {get_response.json().get('customerName')}"
        )

        logger.info(f"Successfully retrieved order: {get_response.json()}")
