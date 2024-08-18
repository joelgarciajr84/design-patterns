from heroes import IronMan, Batman


class HeroesFactory():

    @staticmethod
    def create_hero(hero_type: str):
        if hero_type == 'ironman':
            return IronMan()
        elif hero_type == 'batman':
            return Batman()
        else:
            raise ValueError("Hero not found")
