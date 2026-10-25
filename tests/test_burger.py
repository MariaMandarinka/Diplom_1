import pytest
from unittest.mock import Mock

class TestBurger:
    
    # 1. Тест установки булочки
    def test_set_buns_sets_correct_bun(self, empty_burger, mock_bun):
        empty_burger.set_buns(mock_bun)
        assert empty_burger.bun == mock_bun

    # 2. Тест добавления ингредиента
    def test_add_ingredient_adds_to_ingredients_list(self, empty_burger, mock_ingredient):
        empty_burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in empty_burger.ingredients
        assert len(empty_burger.ingredients) == 1

    # 3. Тест удаления ингредиента (ПОЧИНИТ СТРОКУ 26)
    def test_remove_ingredient_removes_from_list(self, empty_burger, mock_ingredient):
        empty_burger.add_ingredient(mock_ingredient)
        empty_burger.remove_ingredient(0)
        assert mock_ingredient not in empty_burger.ingredients
        assert len(empty_burger.ingredients) == 0

    # 4. Тест перемещения ингредиентов (ПОЧИНИТ СТРОКУ 29)
    def test_move_ingredient_changes_order(self, empty_burger):
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        
        empty_burger.add_ingredient(mock_ing_1)
        empty_burger.add_ingredient(mock_ing_2)
        
        # Меняем их местами
        empty_burger.move_ingredient(0, 1)
        
        assert empty_burger.ingredients[0] == mock_ing_2
        assert empty_burger.ingredients[1] == mock_ing_1

    # 5. Тест расчета стоимости с параметризацией
    @pytest.mark.parametrize(
        "bun_price, ing_price, expected_total",
        [
            (100.0, 50.0, 250.0), 
            (150.5, 99.0, 400.0)
        ]
    )
    def test_get_price_calculates_correct_total(self, empty_burger, bun_price, ing_price, expected_total):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ing_price
        
        empty_burger.set_buns(mock_bun)
        empty_burger.add_ingredient(mock_ingredient)
        
        assert empty_burger.get_price() == expected_total

    # 6. Тест генерации чека
    def test_get_receipt_returns_valid_string(self, empty_burger, mock_bun, mock_ingredient):
        empty_burger.set_buns(mock_bun)
        empty_burger.add_ingredient(mock_ingredient)
        
        receipt = empty_burger.get_receipt()
        
        assert "=== %s ===" % mock_bun.get_name() in receipt
        assert "sauce %s" % mock_ingredient.get_name() in receipt
        assert "Price: 250" in receipt