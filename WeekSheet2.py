class Pet:

    def __init__(self, name: str, animal_type: str, age: int):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Setters (Mutators)
    def set_name(self, name: str):
        self.__name = name

    def set_animal_type(self, animal_type: str):
        self.__animal_type = animal_type

    def set_age(self, age: int):
        self.__age = age

    # Getters (Accessors)
    def get_name(self) -> str:
        return self.__name

    def get_animal_type(self) -> str:
        return self.__animal_type

    def get_age(self) -> int:
        return self.__age


# Program to interact with the user
def main():
    name = input("Enter your pet's name: ")
    animal_type = input("Enter the type of animal: ")
    age = int(input("Enter your pet's age: "))

    pet = Pet(name, animal_type, age)

    # Display pet
    print("\nYour pet's details:")
    print(f"Name: {pet.get_name()}")
    print(f"Type: {pet.get_animal_type()}")
    print(f"Age: {pet.get_age()}")


# Run the program
if __name__ == "__main__":
    main()
