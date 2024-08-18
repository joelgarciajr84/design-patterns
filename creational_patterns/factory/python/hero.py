from abc import ABC, abstractmethod


class HeroInterface(ABC):

    @abstractmethod
    def super_power(self) -> str:
        return str