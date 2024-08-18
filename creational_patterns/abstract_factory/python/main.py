from factory_producer import FactoryProducer

if __name__ == "__main__":
    universe_type = input("Escolha seu universo (marvel, dc): ").lower()

    try:
        factory = FactoryProducer.get_factory(universe_type)

        hero = factory.create_hero()
        villain = factory.create_villain()

        print(f"Você escolheu o universo {universe_type.capitalize()}.")
        print(f"Herói: {hero.super_power()}")
        print(f"Vilão: {villain.evil_plan()}")
    except ValueError as e:
        print(e)
