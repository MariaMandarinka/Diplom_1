import pytest
from praktikum.ingredient import Ingredient
from praktikum.data import TestData


class TestIngredient:
    def test_ingredient_get_type_returns_correct_value(self, default_ingredient):
        assert default_ingredient.get_type() == TestData.INGREDIENT_TYPE

    def test_ingredient_get_name_returns_correct_value(self, default_ingredient):
        assert default_ingredient.get_name() == TestData.INGREDIENT_NAME

    def test_ingredient_get_price_returns_correct_value(self, default_ingredient):
        assert default_ingredient.get_price() == TestData.INGREDIENT_PRICE

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