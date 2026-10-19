import pytest
from praktikum.ingredient import Ingredient

@pytest.fixture
def default_ingredient():
    """Фикстура для создания стандартного ингредиента"""
    return Ingredient("SAUCE", "Соус космический", 50.0)

class TestIngredient:
    def test_ingredient_get_type_returns_correct_value(self, default_ingredient):
        assert default_ingredient.get_type() == "SAUCE"

    def test_ingredient_get_name_returns_correct_value(self, default_ingredient):
        assert default_ingredient.get_name() == "Соус космический"

    def test_ingredient_get_price_returns_correct_value(self, default_ingredient):
        assert default_ingredient.get_price() == 50.0

    # Проверяем параметризацией разные типы ингредиентов (SAUCE и FILLING)
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ("FILLING", "Мясо бессмертных моллюсков", 300.0),
            ("SAUCE", "Space Sauce", 0.0)
        ]
    )
    def test_ingredient_initialization_with_different_types(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price