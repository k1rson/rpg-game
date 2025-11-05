from typing import Optional

from item import Item

class Inventory:
    def __init__(
        self,
        max_slots: int = 10,
    ) -> None:
        
        # Базовые атрибуты
        self.max_slots = max_slots # Сколько разных предметов можно хранить в инвентаре
        self.items = [] # список предметов (объекты Items)
        
    # Внутренний метод: проверяет, есть ли предмет с заданным названием
    def _find_item(self, name: str) -> Optional[Item]:
        for item in self.items:
            if item.name == name:
                return item
            
        return None

    # Добавляет предмет в инвентарь
    def add_item(self, name: str, description: str = "", quantity: int = 1) -> bool:
        existing_item = self._find_item(name=name)
        
        if existing_item is not None:
            existing_item.quantity += quantity
            
            # ТАК ДЕЛАТЬ НЕЛЬЗЯ!!! РЕАЛИЗОВАНО В УЧЕБНЫХ ЦЕЛЯХ!!! СМЕШИВАТЬ ПРЕДСТАВЛЕНИЕ И ЛОГИКУ ЗАПРЕЩЕНО
            print(f"Добавлено {quantity} шт. '{name}'. Теперь в наличии: {existing_item.quantity}")
        else:
            if len(self.items) >= self.max_slots:
                # ТАК ДЕЛАТЬ НЕЛЬЗЯ!!! РЕАЛИЗОВАНО В УЧЕБНЫХ ЦЕЛЯХ!!! СМЕШИВАТЬ ПРЕДСТАВЛЕНИЕ И ЛОГИКУ ЗАПРЕЩЕНО
                print("Инвентарь заполнен! Нельзя добавить новый предмет!")
                return False
            
            new_item = Item(name, description, quantity, max_stack=12) # создаем новый предмет
            self.items.append(new_item) # добавляем наш предмет (объект типа Item) в список!

            # ТАК ДЕЛАТЬ НЕЛЬЗЯ!!! РЕАЛИЗОВАНО В УЧЕБНЫХ ЦЕЛЯХ!!! СМЕШИВАТЬ ПРЕДСТАВЛЕНИЕ И ЛОГИКУ ЗАПРЕЩЕНО
            print(f"Добавлен новый предмет: {name} x{quantity}")
            
        return True
    
    # Удаление указанного количества предмета из инвентаря
    def remove_item(self, name: str, quantity: int = 1) -> bool:
        existing_item = self._find_item(name)
        
        if existing_item is None:
            print(f"Предмет '{name}' не был найден!")
            return False
        
        if existing_item.quantity < quantity:
            print(f"Недостаточно предметов: '{name}'. В наличии: {existing_item.quantity}")
            return False
            
        existing_item.quantity -= quantity
        if existing_item.quantity == 0:
            # Если предмет закончился (равен 0) - удаляем его из инвентаря
            self.items.remove(existing_item)
            print(f"Предмет '{name}' был полностью удален!")
        else:
            print(f"Удалено {quantity} шт. Осталось: {existing_item.quantity}")
        
        return True
