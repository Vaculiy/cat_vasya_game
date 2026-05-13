from abc import ABC, abstractmethod


class Unit(ABC):
    """Класс для всех обьектов"""
    def __init__(
            self, strength, dexterity, telo, wisdom,
            intelligence, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.telo = telo
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    @abstractmethod
    def calculate_max_health(self):
        """Метод, возвращающий значение здоровья."""
        pass

    @abstractmethod
    def calculate_damage(self):
        """Метод, возвращающий значение урона."""        
        pass

    @abstractmethod
    def calculate_defense(self):
        """Метод, возвращающий значение защиты."""        
        pass


class Character(Unit):
    """Класс для характеристик персонажей"""
    def __init__(
            self, strength, dexterity, telo, wisdom,
            intelligence, charisma):
        super().__init__(
                self, strength, dexterity, telo, wisdom,
                intelligence, charisma)

    def calculate_max_health(self):
        """Метод, возвращающий максимальное здоровье персонажа."""
        return int((telo * 10) + strength / 2)

    def calculate_damage(self):
        """Метод, возвращающий полученный урон от противников."""
        return int((strength * 1.5) + dexterity / 4)

    def calculate_defense(self):
        """Метод, возвращающий защиту персонажа."""
        return int((telo * 1.5) + dexterity / 3)


class Monster(Unit):
    """Класс для характеристик противников"""    
    def __init__(
            self, strength, dexterity, telo, wisdom,
            intelligence, charisma):
        super().__init__(
                self, strength, dexterity, telo, wisdom,
                intelligence, charisma)

    def calculate_max_health(self):
        """Метод, возвращающий максимальное здоровье монстра."""
        return int((telo * 8) + strength / 3)

    def calculate_damage(self):
        """Метод, возвращающий получаемый урон от монстра."""
        return int((strength * 2) + telo / 5)

    def calculate_defense(self):
        """Метод, возвращающий защиту монстра."""
        return int((telo * 1) + (0.2 + (strength / 5)))