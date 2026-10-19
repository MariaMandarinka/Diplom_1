import pytest
from praktikum.database import Database

@pytest.fixture
def database_instance():
    """Фикстура возвращает чистый объект базы данных"""
    return Database()

class TestDatabase:
    def test_database_available_buns_returns_not_empty_list(self, database_instance):
        buns = database_instance.available_buns()
        assert len(buns) > 0
        # Проверяем, что элементы в списке действительно имеют метод get_name (т.е. это объекты Bun)
        assert hasattr(buns[0], 'get_name')

    def test_database_available_ingredients_returns_not_empty_list(self, database_instance):
        ingredients = database_instance.available_ingredients()
        assert len(ingredients) > 0
        # Проверяем, что элементы в списке — это объекты Ingredient
        assert hasattr(ingredients[0], 'get_name')
        assert hasattr(ingredients[0], 'get_type')