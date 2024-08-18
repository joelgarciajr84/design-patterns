from abstract_hero_factory import AbstractHeroFactory
from heroes import WonderWoman, Cheetah

class DCFactory(AbstractHeroFactory):
    def create_hero(self):
        return WonderWoman()

    def create_villain(self):
        return Cheetah()
