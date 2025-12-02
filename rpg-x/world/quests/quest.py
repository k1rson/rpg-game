from entities.player.player import PlayerEntity


class Quest:
    def __init__(
        self, qid: int, name: str, description: str, requirements: dict, reward: dict
    ) -> None:
        # Инициализация базовых атрибутов класса
        self.id = qid  # уникальный ID квеста
        self.name = name  # название квеста
        self.description = description  # описание квеста
        self.requirements = requirements  # требования к выполнению -> dict: {"has_item": "Ключ", "visited": "Город"}
        self.reward = reward  # награда за квест -> dict: {"item": Item}

        self.active = False
        self.completed = False

    # Методы классса (поведение класса)
    # Проверяет, выполнен ли квест
    def can_complete(self, player: PlayerEntity):
        if "has_item" in self.requirements:
            item = self.requirements["has_item"]
            if item not in player.inventory:
                return False

        return True

        # Проверка по нахождению в локации
        # Иные проверки на выполнение квеста

    # Выполнить квест -> выдать награду
    def complete(self, player: PlayerEntity):
        if not self.completed and self.can_complete(player):
            self.completed = True

            # Проверка на выдаваемую награду
            if "item" in self.reward:
                player.inventory.add_item(self.reward["item"])

            return True

        return False
