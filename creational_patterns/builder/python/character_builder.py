from abc import ABC, abstractmethod
from hero import Hero
from villain import Villain


class HeroBuilderInterface(ABC):
    def __init__(self):
        self.hero = Hero()

    @abstractmethod
    def build_name(self):
        pass

    @abstractmethod
    def build_super_power(self):
        pass

    @abstractmethod
    def build_alignment(self):
        pass

    @abstractmethod
    def build_origin(self):
        pass

    def get_hero(self):
        return self.hero


class VillainBuilderInterface(ABC):
    def __init__(self):
        self.villain = Villain()

    @abstractmethod
    def build_name(self):
        pass

    @abstractmethod
    def build_evil_plan(self):
        pass

    @abstractmethod
    def build_alignment(self):
        pass

    @abstractmethod
    def build_origin(self):
        pass

    def get_villain(self):
        return self.villain


class SuperHeroBuilder(HeroBuilderInterface):
    def build_name(self):
        self.hero.name = "Superman"

    def build_super_power(self):
        self.hero.super_power = "Super-força, voo, visão de calor"

    def build_alignment(self):
        self.hero.alignment = "Herói"

    def build_origin(self):
        self.hero.origin = "Planeta Krypton"


class VillainBuilder(VillainBuilderInterface):
    def build_name(self):
        self.villain.name = "Lex Luthor"

    def build_evil_plan(self):
        self.villain.evil_plan = "Dominar o mundo com tecnologia avançada"

    def build_alignment(self):
        self.villain.alignment = "Vilão"

    def build_origin(self):
        self.villain.origin = "Metrópolis"
