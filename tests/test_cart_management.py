# tests/test_cart_management.py

import pytest

@pytest.mark.cart_management
def test_update_cart_quantity(setup_cart_with_item):
    """
    This test verifies that the quantity of an item in the cart can be updated.
    """
    print("--- Starting test: test_update_cart_quantity ---")
    cart_screen, _ = setup_cart_with_item

    cart_screen.increase_quantity()
    
    assert cart_screen.wait_for_cart_quantity_to_be("2"), "Cart quantity did not update to 2."

@pytest.mark.cart_management
def test_remove_item_from_cart(setup_cart_with_item):
    """
    This test verifies that an item can be removed from the cart.
    """
    print("--- Starting test: test_remove_item_from_cart ---")
    cart_screen, _ = setup_cart_with_item
    
    cart_screen.remove_item()
    assert not cart_screen.is_backpack_in_cart(), "Item was not successfully removed from the cart."

@pytest.mark.cart_management
@pytest.mark.edge_case
def test_decrease_quantity_removes_item(setup_cart_with_item):
    """
    This edge case test verifies that decreasing the quantity of an item
    from 1 removes it from the cart.
    """
    print("--- Starting test: test_decrease_quantity_removes_item ---")
    cart_screen, _ = setup_cart_with_item

    # The fixture sets up the cart with 1 item. Now, decrease the quantity.
    cart_screen.decrease_quantity()

    # Assert that the cart is now empty
    assert cart_screen.is_cart_empty(), "Decreasing quantity from 1 did not empty the cart."

