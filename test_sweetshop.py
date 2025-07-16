import pytest
from sweetshop import SweetShop

# Fixture to create a fresh test database before each test
@pytest.fixture
def shop():
    # Use test DB and clear any existing data
    s = SweetShop("test_sweetshop.db")
    s.clear_all()
    return s

# Test: Add a sweet
def test_add_sweet(shop):
    shop.add_sweet(1, "Kaju Katli", "Nut-Based", 100, 10)
    sweets = shop.view_all_sweets()
    assert sweets[0]["name"] == "Kaju Katli"

# Test: Delete a sweet
def test_delete_sweet(shop):
    shop.add_sweet(1, "Kaju Katli", "Nut-Based", 100, 10)
    shop.delete_sweet(1)
    sweets = shop.view_all_sweets()
    assert len(sweets) == 0

# Test: View all sweets
def test_view_all_sweets(shop):
    shop.add_sweet(1, "Kaju Katli", "Nut-Based", 100, 10)
    shop.add_sweet(2, "Gulab Jamun", "Milk-Based", 50, 20)
    sweets = shop.view_all_sweets()
    assert len(sweets) == 2

# Test: Search by name
def test_search_by_name(shop):
    shop.add_sweet(1, "Kaju Katli", "Nut-Based", 100, 10)
    shop.add_sweet(2, "Gulab Jamun", "Milk-Based", 50, 20)
    result = shop.search_sweets(name="Gulab Jamun")
    assert len(result) == 1
    assert result[0]["name"] == "Gulab Jamun"

# Test: Search by category
def test_search_by_category(shop):
    shop.add_sweet(1, "Kaju Katli", "Nut-Based", 100, 10)
    result = shop.search_sweets(category="Nut-Based")
    assert result[0]["category"] == "Nut-Based"

# Test: Search by price range
def test_search_by_price_range(shop):
    shop.add_sweet(1, "Kaju Katli", "Nut-Based", 100, 10)
    shop.add_sweet(2, "Gulab Jamun", "Milk-Based", 50, 20)
    result = shop.search_sweets(min_price=40, max_price=60)
    assert len(result) == 1
    assert result[0]["name"] == "Gulab Jamun"

# Test: Purchase sweet successfully
def test_purchase_sweet_success(shop):
    shop.add_sweet(1, "Kaju Katli", "Nut-Based", 100, 10)
    shop.purchase_sweet(1, 3)
    sweets = shop.view_all_sweets()
    assert sweets[0]["quantity"] == 7

# Test: Purchase sweet - insufficient stock error
def test_purchase_sweet_insufficient_stock(shop):
    shop.add_sweet(1, "Kaju Katli", "Nut-Based", 100, 2)
    with pytest.raises(ValueError) as e:
        shop.purchase_sweet(1, 5)
    assert str(e.value) == "Not enough stock available"

# Test: Restock a sweet
def test_restock_sweet(shop):
    shop.add_sweet(1, "Kaju Katli", "Nut-Based", 100, 5)
    shop.restock_sweet(1, 10)
    sweets = shop.view_all_sweets()
    assert sweets[0]["quantity"] == 15

# Test: Sort sweets by price (ascending)
def test_sort_sweets_by_price(shop):
    shop.add_sweet(1, "Kaju Katli", "Nut-Based", 100, 10)
    shop.add_sweet(2, "Gulab Jamun", "Milk-Based", 50, 20)
    sorted_sweets = shop.sort_sweets("price")
    sorted_ids = list(sorted_sweets.keys())
    assert sorted_ids == [2, 1]  # Sorted by price ascending
