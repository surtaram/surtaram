import pytest
import allure

from conftest import logger
from helper.requests.create_order import CreateOrder


@allure.epic("Submit a new order")
@allure.feature("Create Order Feature")
class TestCreateOrder:

    @pytest.mark.order(1)
    @allure.story("Submit a new order")
    @allure.title("Test Submit Order")
    @allure.description("Test to submit a new order and verify the response.")
    def test_submit_order(self):
        """
        Test to submit a new order and verify the response.
        """
        # Step 1: Make a POST request to submit a new order
        response = CreateOrder.create_order()

        # Step 2: Handle potential response errors
        if response is None:
            logger.error("Failed to submit a new order.")
            pytest.fail("Failed to submit a new order.")

        # Step 3: Log and verify the successful submission of the order
        order_id = response.json().get('orderId')  # Safely get the order ID
        logger.info(f"Successfully submitted new order with ID: {order_id}")

        # Step 4: Verify that the order was created successfully
        assert response.json().get(
            'created') is True, f"Expected 'created' to be True but got {response.json().get('created')}"
        assert order_id is not None, "Expected 'orderId' to be not None but it was None."

        logger.info(f"Successfully retrieved order: {response.json()}")
