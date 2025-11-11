from typing import Optional

from inventory.items.base import BaseItem


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
        if not isinstance(item, BaseItem):
            raise TypeError(
                "Многоуважаемый игрок! Нельзя запихивать Рафика и самого себя в инвентарь!"
            )

        existing = self._find_item_by_name(name=item.name)
        if existing is not None:
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

    def remove_item(self, item_name: str, count: int = 1) -> list[BaseItem]:
        pass

    def has_item(self, item_name: str) -> bool:
        pass

    # Проверяет, заполен ли инвентарь (проверка идет по слотам)
    def is_full(self) -> bool:
        return len(self.items) >= self.max_slots

    def show(self):
        pass

    def use_item(self, item_name: str, entity: BaseEntity) -> bool:
        pass
