import pytest
from praktikum.bun import Bun

@pytest.fixture
def default_bun():
    """Фикстура для создания стандартной булочки"""
    return Bun("Краторная булка", 100.0)

class TestBun:
    def test_bun_get_name_returns_correct_value(self, default_bun):
        assert default_bun.get_name() == "Краторная булка"

    def test_bun_get_price_returns_correct_value(self, default_bun):
        assert default_bun.get_price() == 100.0

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