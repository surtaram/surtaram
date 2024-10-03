import pytest
import allure

from conftest import logger
from helper.requests.create_order import CreateOrder
from helper.requests.update_order import UpdateOrder
from helper.requests.get_order import GetOrder


@allure.epic("Update an order")
@allure.feature("Update Order Feature")
class TestUpdateBook:

    @pytest.mark.order(1)
    @allure.story("Update an existing order")
    @allure.title("Test Update Order")
    @allure.description("Test to create a new order, update it, and verify the changes.")
    def test_update_order(self):
        """
        Test to create a new order, update it, and verify the changes.
        """
        # Create a new order and handle errors
        post_response = CreateOrder.create_order()
        if post_response is None:
            logger.error("Failed to create a new order.")
            pytest.fail("Failed to create a new order.")

        order_id = post_response.json().get('orderId')  # Safely access orderId
        logger.info(f"New order created with ID: {order_id}")

        # Update the order and handle errors
        patch_response = UpdateOrder.update_order(order_id)
        if patch_response is None:
            logger.error(f"Failed to update order with ID: {order_id}")
            pytest.fail(f"Failed to update order with ID: {order_id}")

        # Fetch the updated order and handle errors
        get_response = GetOrder.get_order_by_id(order_id)
        if get_response is None:
            logger.error(f"Failed to retrieve updated order with ID: {order_id}")
            pytest.fail(f"Failed to retrieve updated order with ID: {order_id}")

        # Assertions to verify the updated values
        assert get_response.json().get('bookId') == 1, (
            f"Expected 'bookId' to be 1 but got {get_response.json().get('bookId')}"
        )
        assert get_response.json().get('customerName') == 'automation user updated', (
            f"Expected 'customerName' to be 'automation user updated' but got {get_response.json().get('customerName')}"
        )

        logger.info(f"Successfully retrieved updated order: {get_response.json()}")
