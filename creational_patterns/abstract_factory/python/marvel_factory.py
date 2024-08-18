from abstract_hero_factory import AbstractHeroFactory
from heroes import SpiderMan, GreenGoblin

class MarvelFactory(AbstractHeroFactory):
    def create_hero(self):
        return SpiderMan()

    def create_villain(self):
        return GreenGoblin()
