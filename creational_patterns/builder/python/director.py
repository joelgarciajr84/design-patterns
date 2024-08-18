from character_builder import HeroBuilderInterface, VillainBuilderInterface

class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_character(self):
        self._builder.build_name()
        if isinstance(self._builder, HeroBuilderInterface):
            self._builder.build_super_power()
        elif isinstance(self._builder, VillainBuilderInterface):
            self._builder.build_evil_plan()
        self._builder.build_alignment()
        self._builder.build_origin()
