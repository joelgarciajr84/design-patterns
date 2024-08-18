class Villain:
    def __init__(self):
        self.name = None
        self.evil_plan = None
        self.alignment = None
        self.origin = None

    def __str__(self):
        return (f"Vilão: {self.name}, Plano: {self.evil_plan}, "
                f"Alinhamento: {self.alignment}, Origem: {self.origin}")
