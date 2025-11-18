from ..entities.base import BaseEntity
from .effect import BaseEffect


class AttackEffect(BaseEffect):
    def __init__(self, name: str, duration: int, attack_bonus: float) -> None:
        super().__init__(name, duration)

        if attack_bonus <= 0:
            raise ValueError("Бонус на атаку не может быть меньше либо равен 0!")

        # Инициализация базовых характеристик эффекта
        self.attack_bonus = attack_bonus
        self._original_attack: float = 0.0

    def on_apply(self, entity: BaseEntity) -> None:
        self._original_attack = entity.attack
        entity.attack += self.attack_bonus

    def on_tick(self, entity: BaseEntity) -> None:
        pass

    def on_remove(self, entity: BaseEntity) -> None:
        if self._original_attack <= 0:
            raise ValueError(
                "Невозможно восстановить атаку, она не может быть меньше либо равна 0"
            )

        entity.attack = self._original_attack


class PoisonEffect(BaseEffect):
    def __init__(self, name: str, duration: int, damage_per_tern: float) -> None:
        super().__init__(name, duration)

        if damage_per_tern <= 0:
            raise ValueError("Урон от яда не может быть меньше либо равен 0!")

        # Инициализация базовых характеристик эффекта
        self.damage_per_tern = damage_per_tern

    def on_apply(self, entity: BaseEntity) -> None:
        pass

    def on_tick(self, entity: BaseEntity) -> None:
        entity.take_damage(self.damage_per_tern)
        print(
            f"{entity.name} получает {self.damage_per_tern} урона от {self.name} (осталось: {self.duration})"
        )

    def on_remove(self, entity: BaseEntity) -> None:
        pass


class HealOverTime(BaseEffect):  # эффект заживления ран
    def __init__(self, name: str, duration: int, heal_per_tern: float) -> None:
        super().__init__(name, duration)

        if heal_per_tern <= 0:
            raise ValueError(
                "Значение восстановления здоровья не может быть меньше либо равно 0!"
            )

        # Инициализация базовых характеристик эффекта
        self.heal_per_tern = heal_per_tern

    def on_apply(self, entity: BaseEntity) -> None:
        pass

    def on_tick(self, entity: BaseEntity) -> None:
        entity.heal(self.heal_per_tern)
        print(
            f"{entity.name} получает {self.heal_per_tern} ХП от {self.name} (осталось: {self.duration})"
        )

    def on_remove(self, entity: BaseEntity) -> None:
        pass


class ShieldBuff(BaseEffect):  # разовый буст для щита
    def __init__(self, name: str, duration: int, shield_bonus: float) -> None:
        super().__init__(name, duration)

        if shield_bonus <= 0:
            raise ValueError("Бонус на щит  не может быть меньше либо равен 0!")

        # Инициализация базовых характеристик эффекта
        self.shield_bonus = shield_bonus
        self._origin_shield: float = 0.0

    def on_apply(self, entity: BaseEntity) -> None:
        self._origin_shield = entity.shield
        entity.shield += self.shield_bonus

    def on_tick(self, entity: BaseEntity) -> None:
        pass

    def on_remove(self, entity: BaseEntity) -> None:
        if self._origin_shield <= 0:
            raise ValueError(
                "Невозможно восстановить щит, он не может быть меньше либо равен 0"
            )

        entity.shield = self._origin_shield


class CritChanceDebuff(BaseEffect):  # разовый дебафф для крит. шанса
    def __init__(self, name: str, duration: int) -> None:
        super().__init__(name, duration)

    def on_apply(self, entity: BaseEntity) -> None:
        return super().on_apply(entity)

    def on_tick(self, entity: BaseEntity) -> None:
        return super().on_tick(entity)

    def on_remove(self, entity: BaseEntity) -> None:
        return super().on_remove(entity)


class CritChanceBuff(BaseEffect):  # разовый бафф для крит. шанса
    def __init__(self, name: str, duration: int) -> None:
        super().__init__(name, duration)

    def on_apply(self, entity: BaseEntity) -> None:
        return super().on_apply(entity)

    def on_tick(self, entity: BaseEntity) -> None:
        return super().on_tick(entity)

    def on_remove(self, entity: BaseEntity) -> None:
        return super().on_remove(entity)
