import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.data import TestData
from praktikum.ingredient import Ingredient  # <-- Добавили импорт ингредиента!
from praktikum.database import Database       # <-- Добавили импорт базы данных!

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

@pytest.fixture
def default_bun():
    """Фикстура использует централизованные данные из пакета praktikum"""
    return Bun(TestData.BUN_NAME, TestData.BUN_PRICE)

@pytest.fixture
def default_ingredient():
    """Фикстура для ингредиента, перенесенная по замечанию ревьюера"""
    return Ingredient(
        TestData.INGREDIENT_TYPE, 
        TestData.INGREDIENT_NAME, 
        TestData.INGREDIENT_PRICE
    )

@pytest.fixture
def database_instance():
    """Фикстура возвращает чистый объект базы данных, перенесенная по ревью"""
    return Database()