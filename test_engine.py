# test_engine.py
import pytest

# Импортируем класс двигателя.



# engine_class.py
class Engine:
    """Класс двигателя."""

    def __init__(self):
        # При создании объекта двигателя он не запущен.
        self.is_running = False

@pytest.fixture
def engine():
    """Фикстура возвращает экземпляр класса двигателя."""
    return Engine()


# Эта фикстура не возвращает никаких значений, но изменяет объект,
# созданный другой фикстурой.
@pytest.fixture
def start_engine(engine):  # Вызываем фикстуру получения объекта двигателя.
    """Фикстура запускает двигатель."""
    # Изменяем значение свойства объекта:
    engine.is_running = True


def test_engine_is_running(engine, start_engine):  # Вызываем обе фикстуры.
    """Тест проверяет, работает ли двигатель."""
    assert engine.is_running  # Проверяем, что значение атрибута is_running это True.