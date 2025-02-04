class Car:

    def __init__(self, year_model: int, make: str):

        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  # Initial speed is always 0

    # Method to increase speed
    def accelerate(self):

        self.__speed += 5

    # Method to decrease speed
    def brake(self):

        self.__speed = max(0, self.__speed - 5)  # Ensures speed never goes negative

    # Getter for speed
    def get_speed(self) -> int:

        return self.__speed


# Program to interact with the user
def main():

    car = Car(2022, "Toyota")

    # Accelerate five times
    print("Accelerating...")
    for _ in range(5):
        car.accelerate()
        print(f"Current speed: {car.get_speed()} mph")

    # Brake five times
    print("\nBraking...")
    for _ in range(5):
        car.brake()
        print(f"Current speed: {car.get_speed()} mph")


# Run the program
if __name__ == "__main__":
    main()
