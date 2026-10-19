import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.fixture
def empty_burger():
    """Фикстура возвращает свежий чистый объект бургера для каждого теста"""
    return Burger()

@pytest.fixture
def mock_bun():
    """Фикстура возвращает настроенный мок булочки"""
    bun = Mock()
    bun.get_name.return_value = "Краторная булка"
    bun.get_price.return_value = 100.0
    return bun

@pytest.fixture
def mock_ingredient():
    """Фикстура возвращает настроенный мок ингредиента (соуса)"""
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "Соус космический"
    ingredient.get_price.return_value = 50.0
    return ingredient