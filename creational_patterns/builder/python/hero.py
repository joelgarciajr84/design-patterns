
class Hero:
    def __init__(self):
        self.name = None
        self.super_power = None
        self.alignment = None
        self.origin = None

    def __str__(self):
        return (f"Herói: {self.name}, Poder: {self.super_power}, "
                f"Alinhamento: {self.alignment}, Origem: {self.origin}")
