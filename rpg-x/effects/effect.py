from abc import ABC, abstractmethod

from entities.base import BaseEntity


class BaseEffect(ABC):
    """
        Базовый класс для всех временных эффектов
    Args:
        name: str -> название эффеекта (для отображения)
        duration: int -> продолжительность эффекта (длительность в ходах)
    """

    def __init__(self, name: str, duration: int) -> None:
        # Валидация базовых атрибутов
        if duration <= 0:
            raise ValueError("Длительность эффекта не может быть меньше либо равно 0!")

        # Инициализация базовых атрибутов
        self.name = name
        self.duration = duration

    # Реализация базовых методов для наследования

    # Применение эффекта один раз
    @abstractmethod  # декоратор
    def on_apply(self, entity: BaseEntity) -> None:
        pass

    # Применение эффекта на несколько ходов
    @abstractmethod  # декоратор
    def on_tick(self, entity: BaseEntity) -> None:
        pass

    # Снятие эффекта с сущности
    @abstractmethod  # декоратор
    def on_remove(self, entity: BaseEntity) -> None:
        pass

    # Магический метод для человекочитаемого отображения объекта класса
    def __str__(self) -> str:
        return f"{self.name} ({self.duration} ходов)"
