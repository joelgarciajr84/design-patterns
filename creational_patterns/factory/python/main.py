from heroes_factory import HeroesFactory

if __name__ == "__main__":
    hero_type = input("Escolha seu herói (batman, ironman): ").lower()
    
    try:
        hero = HeroesFactory.create_hero(hero_type)
        print(f"Você escolheu {hero_type.capitalize()}. Poder especial: {hero.super_power()}")
    except ValueError as e:
        print(e)
