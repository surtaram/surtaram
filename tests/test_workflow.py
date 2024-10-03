import pytest
import allure

from conftest import logger
from helper.requests.create_order import CreateOrder
from helper.requests.update_order import UpdateOrder
from helper.requests.get_order import GetOrder
from helper.requests.delete_order import DeleteOrder


@allure.epic("End-to-end order management workflow")
@allure.feature("Order Workflow")
class TestWorkFlow:

    @pytest.mark.order(1)
    @allure.story("End-to-end order management workflow")
    @allure.title("Test Order Workflow")
    @allure.description("End-to-end workflow test: Create, Update, Retrieve, and Delete an order.")
    def test_workflow(self):
        """
        End-to-end workflow test:
        1. Create a new order (POST)
        2. Update the order (PATCH)
        3. Retrieve the updated order (GET)
        4. Delete the order (DELETE)
        """

        # Step 1: Create a new order
        post_response = CreateOrder.create_order()
        assert post_response, "Failed to create a new order."
        order_id = post_response.json().get('orderId')
        logger.info(f"Created order with ID: {order_id}")

        # Step 2: Update the order
        patch_response = UpdateOrder.update_order(order_id)
        assert patch_response.status_code == 204, "Failed to update the order."
        logger.info(f"Updated order with ID: {order_id}")

        # Step 3: Retrieve the updated order
        get_response = GetOrder.get_order_by_id(order_id)
        assert get_response.json().get('customerName') == 'automation user updated', (
            f"Expected 'customerName' to be 'automation user updated' but got {get_response.json().get('customerName')}"
        )
        logger.info(f"Retrieved updated order: {get_response.json()}")

        # Step 4: Delete the order
        delete_response = DeleteOrder.delete_order(order_id)
        assert delete_response.status_code == 204, "Failed to delete the order."
        logger.info(f"Deleted order with ID: {order_id}")
