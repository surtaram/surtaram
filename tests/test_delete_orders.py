ximport pytest
import allure

from conftest import logger
from helper.requests.create_order import CreateOrder
from helper.requests.delete_order import DeleteOrder


@allure.epic("Delete an order")
@allure.feature("Delete Order Feature")
class TestDeleteOrder:

    @pytest.mark.order(1)
    @allure.story("Delete an existing order")
    @allure.title("Test Delete Order")
    @allure.description("Test to create a new order and then delete it by ID to verify the deletion.")
    def test_delete_order(self):
        """
        Test to create a new order and then delete it by ID to verify the deletion.
        """
        # Create a new order
        post_response = CreateOrder.create_order()
        if post_response is None:
            logger.error("Failed to create a new order.")
            pytest.fail("Failed to create a new order.")

        order_id = post_response.json().get('orderId')
        logger.info(f"New order created with ID: {order_id}")

        # Delete the order using the fetched order ID
        delete_response = DeleteOrder.delete_order(order_id)
        if delete_response is None:
            logger.error(f"Failed to delete order with ID: {order_id}")
            pytest.fail(f"Failed to delete order with ID: {order_id}")

        # Assert to verify the deletion was successful
        assert delete_response.status_code == 204, (
            f"Expected status code to be 204 but received {delete_response.status_code}"
        )
        logger.info("Successfully deleted order")
