from hero import HeroInterface

class Batman(HeroInterface):

    def super_power(self) -> str:
        return "Detetive super inteligente"


class IronMan(HeroInterface):

    def super_power(self) -> str:
        return "Genio da computacao"
