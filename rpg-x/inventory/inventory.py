from typing import Optional

from inventory.items.base import BaseItem
from entities.base import BaseEntity


class Inventory:
    def __init__(
        self,
        max_slots: int = 10,
    ) -> None:
        # Базовые атрибуты
        self.max_slots = max_slots  # Сколько разных предметов можно хранить в инвентаре
        self.items = []  # список предметов (объекты Items)

    # Внутренние методы
    # Поиск предмета в инвентаре по ИМЕНИ
    def _find_item_by_name(self, name: str) -> Optional[BaseItem]:
        for item in self.items:
            if item.name == name:
                return item
        return None

    # Поиск предмета в инвентаре по ИНДЕКСУ
    def _find_item_by_index(self, index: int) -> Optional[BaseItem]:
        pass

    # Добавление предмета в инвентарь
    def add_item(self, item: BaseItem) -> bool:
        # проверка на то, чтобы переменная item, которую мы передаем в функцию была либо типа BaseItem или его наследником
        if not isinstance(item, BaseItem):
            raise TypeError(
                "Многоуважаемый игрок! Нельзя запихивать Рафика и самого себя в инвентарь!"
            )

        existing = self._find_item_by_name(name=item.name)
        if existing is not None:  # проверка на наличие предмета
            # НИЖЕ ПРОВЕРКА НА РАЗНЫЕ ТИПЫ. ЕСЛИ ЭТО РАЗНЫЕ ТИПЫ, СТАКАТЬ ПРЕДМЕТЫ НЕЛЬЗЯ
            if existing.__class__ is not item.__class__:
                if self.is_full():  # инвентарь полный, добавить ничего не можем
                    print(
                        "Инвентарь заполнен! Добавить новый предмет нельзя! Рафик негодует"
                    )
                    return False

                self.items.append(item)
                return True

            # ЕСЛИ ПРЕДМЕТЫ ОДИНАКОВЫЕ, ТО МЫ МОЖЕМ ИХ СТАКАТЬ
            new_quantity = existing.quantity + item.quantity
            if new_quantity <= existing.max_stack:
                existing.quantity = new_quantity
                return True
            else:
                # определяем свободного места в стаке, сколько можно добавить
                free_space = existing.max_stack - existing.quantity
                if free_space > 0:
                    existing.quantity = existing.max_stack
                    # Остаток можно добавить, как новый предмет!

                return False
        else:
            if self.is_full():  # инвентарь заполен
                print(
                    "Инвентарь заполнен! Добавить новый предмет нельзя! Рафик негодует"
                )
                return False
            self.items.append(item)
            return True

    # Данный метод удаляет указанное количество предметов из инвентаря по ИМЕНИ предмета
    def remove_item(self, item_name: str, count: int = 1) -> bool:
        if count <= 0:
            return False

        item = self._find_item_by_name(name=item_name)  # ищем предмет по имени
        if item is None:
            return False

        # проверяем количество предметов хватает для удаления или нет
        if item.quantity < count:
            return False

        item.quantity -= count  # удаляем указанное количество предметов

        # если предметов стало меньше либо равно 0, то полностью удаляем предмет из инвентаря
        if item.quantity <= 0:
            self.items.remove(item)

        return True

    # Проверяет, есть ли указанное количество предметов в инвентаре
    def has_item(self, item_name: str, count: int = 1) -> bool:
        item = self._find_item_by_name(name=item_name)

        # (ПРЕДМЕТ ЕСТЬ) AND (КОЛ-ВО ПРЕДМЕТОВ БОЛЬШЕ ЗАПРАШИВАЕМОГО)
        # если два условия True, то результат тоже True
        # если хотя бы одно из условий False -> функция вернет False
        return item is not None and item.quantity >= count

    # Возвращает ВСЕ предметы, которые подходят под УКАЗАННЫЙ ТИП
    def get_items_by_type(self, item_type) -> list[BaseItem]:
        return [item for item in self.items if isinstance(item, item_type)]

    # Проверяет, заполен ли инвентарь (проверка идет по слотам)
    def is_full(self) -> bool:
        return len(self.items) >= self.max_slots

    # Возврещение строкового представления инвентаря
    def show(self):
        pass

    def use_item(self, item_name: str, entity: BaseEntity) -> bool:
        pass
