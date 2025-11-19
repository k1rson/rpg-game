import random

from typing import Optional, Type

from entities.base import BaseEntity
from inventory.items.base import BaseItem


class BaseLocation:
    def __init__(
        self,
        name: str,
        description: str,
        enemy_types: Optional[list[Type[BaseEntity]]] = None,
        enemy_spawn_chance: float = 0.7,
        max_enemies: int = 3,
        loot_table: Optional[list[Type[BaseItem]]] = None,
        loot_spawn_chance: float = 0.5,
        max_loot: int = 10,
        respawn_time: int = 3,  # через сколько будет респавниваться локация (0 - никогда)
    ) -> None:
        # Базовая информация о локации
        self.name = name
        self.description = description

        # Враги
        self.enemy_types = enemy_types
        self.enemy_spawn_chance = enemy_spawn_chance
        self.max_enemies = max_enemies

        # Лут
        self.loot_table = loot_table
        self.loot_spawn_chance = loot_spawn_chance
        self.max_loot = max_loot

        # Респавн локации
        self.respawn_time = respawn_time
        self._visits_since_respawn = 0

        # Текущее состояние локации (данное состояние будет генерироваться перед каждым входом в локацию)
        self.current_enemies: list[BaseEntity] = []
        self.current_loot: list[BaseItem] = []

    # Внутренние методы класса
    # Метод отвечает за генерацию контента на локации (враги/лут)
    def _generate_content(self) -> None:
        self.current_enemies = []
        self.current_loot = []

        # Генерация врагов
        if self.enemy_types and random.random() < self.enemy_spawn_chance:
            num_enemies = random.randint(
                1, min(self.max_enemies, len(self.enemy_types))
            )

            for _ in range(num_enemies):
                enemy_class = random.choice(self.enemy_types)

                enemy = enemy_class(
                    name="Дикий Вепрь",  # TODO пофиксить статичное имя
                    age=random.randint(1, 10),
                    gender=random.choice(["М", "Ж"]),
                    entity_type="Enemy",
                )

                self.current_enemies.append(enemy)

        # Генерация лута
        if self.loot_table and random.random() < self.loot_spawn_chance:
            num_loot = random.randint(1, min(self.max_loot, len(self.loot_table)))

            for _ in range(num_loot):
                loot_class = random.choice(self.loot_table)

                loot = loot_class(  # TODO пофиксить генерацию лута
                    name=f"{loot_class.__name__}",
                    description="Лучший предмет в игре",
                    stackable=True,
                )

                self.current_loot.append(loot)

    # Базовые методы (поведение каждой локации)
    # Вызывается при входе на локацию и генерирует контент
    def enter(self) -> None:
        self._visits_since_respawn += 1

        # Если respawn_time == 0, то локация считается статичной, то-есть, никогда не генерируется заново
        if self.respawn_time == 0:
            return

        if self._visits_since_respawn >= self.respawn_time or not self.current_enemies:
            # Генерируем новую локацию
            self._generate_content()
        else:
            # Сохраняем состояние локации
            pass

    # Метод, позволяющий подбирать предмет с локации по индексу
    def take_loot(self, index: int) -> Optional[BaseItem]:
        if 0 <= index < len(self.current_loot):
            return self.current_loot.pop(index)
        return None

    # Метод, позволяющий показать какой лут находится сейчас на локации
    def display_loot(self) -> str:
        if not self.current_loot:
            return f"В локации {self.name} ничего нет! Рафик все сьел"

        lines = ["Вы видите на земле: "]
        for i, item in enumerate(self.current_loot, 1):
            lines.append(f"{i}. {item.name}")

        return "\n".join(lines)

    # Метод, позволяющий показать какие враги сейчас находятся на локации
    def display_enemies(self) -> str:
        if not self.current_enemies:
            return f"В локации {self.name} никого нет! Рафик всех сьел"

        lines = ["Вы видите вокруг себя: "]
        for i, enemy in enumerate(self.current_enemies, 1):
            lines.append(f"👽 {i}. {enemy.name} | {enemy.level}")

        return "\n".join(lines)
