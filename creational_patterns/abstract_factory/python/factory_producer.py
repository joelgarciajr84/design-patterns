from marvel_factory import MarvelFactory
from dc_factory import DCFactory

class FactoryProducer:
    @staticmethod
    def get_factory(universe_type):
        if universe_type == "marvel":
            return MarvelFactory()
        elif universe_type == "dc":
            return DCFactory()
        else:
            raise ValueError(f"Universe '{universe_type}' não reconhecido.")
