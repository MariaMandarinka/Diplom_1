import pytest
from praktikum.bun import Bun
from praktikum.data import TestData  # Импортируем класс с данными

class TestBun:
    def test_bun_get_name_returns_correct_value(self, default_bun):
        assert default_bun.get_name() == TestData.BUN_NAME

    def test_bun_get_price_returns_correct_value(self, default_bun):
        assert default_bun.get_price() == TestData.BUN_PRICE

    # Проверяем разные граничные значения через параметризацию
    @pytest.mark.parametrize(
        "name, price",
        [
            ("Флюоресцентная булка", 999.99),
            ("Булка с кунжутом", 0.0),
            ("A", -5.0)  # Проверка на отрицательную цену, если логика класса это позволяет
        ]
    )
    def test_bun_initialization_with_different_values(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price