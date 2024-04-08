class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)


def main():
    vehicle_type = "car"  # Set default vehicle type to car
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sunroof): ")

    # Validate doors input
    while doors not in ["2", "4"]:
        doors = input("Enter 2 or 4 for the number of doors: ")

    # Validate roof input
    while roof.lower() not in ["solid", "sunroof"]:
        roof = input("Enter solid or sunroof for the type of roof: ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)
    print("\nCar information:")
    car.display_info()


if __name__ == "__main__":
    main()