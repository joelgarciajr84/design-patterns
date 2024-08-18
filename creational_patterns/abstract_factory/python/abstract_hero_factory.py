from abc import ABC, abstractmethod

class AbstractHeroFactory(ABC):
    @abstractmethod
    def create_hero(self):
        pass

    @abstractmethod
    def create_villain(self):
        pass
