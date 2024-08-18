from character_builder import SuperHeroBuilder, VillainBuilder
from director import Director

def main():
    choice = input("Você quer construir um herói ou vilão? (heroi/vilao): ").lower()

    if choice == "heroi":
        builder = SuperHeroBuilder()
        print("Construindo herói...")
    elif choice == "vilao":
        builder = VillainBuilder()
        print("Construindo vilão...")
    else:
        print("Escolha inválida!")
        return

    director = Director(builder)
    director.construct_character()

    if choice == "heroi":
        character = builder.get_hero()
        print("\nHerói Construído:")
        print(character)
    else:
        character = builder.get_villain()
        print("\nVilão Construído:")
        print(character)

if __name__ == "__main__":
    main()
