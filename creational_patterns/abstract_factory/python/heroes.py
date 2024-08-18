from abc import ABC, abstractmethod

class Hero(ABC):
    @abstractmethod
    def super_power(self):
        pass

class Villain(ABC):
    @abstractmethod
    def evil_plan(self):
        pass

class SpiderMan(Hero):
    def super_power(self):
        return "SipderMan - Lança teias e tem agilidade sobre-humana."

class GreenGoblin(Villain):
    def evil_plan(self):
        return "GreenGoblin - Usa bombas de abóbora e voa em um planador."

class WonderWoman(Hero):
    def super_power(self):
        return "WonderWoman - Super-força, agilidade e usa o laço da verdade."

class Cheetah(Villain):
    def evil_plan(self):
        return "Cheetah - Velocidade e força sobre-humanas para derrotar a Mulher-Maravilha."
