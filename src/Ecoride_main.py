from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    def __init__(self):
        self.hubs = {}  

    def display(self):
        print("Welcome to Eco-Ride Urban Mobility System")

    def add_hub(self):
        hub_name = input("Enter hub name: ")
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' added successfully")
        else:
            print("Hub already exists")

    def add_vehicle_to_hub(self):
        hub_name = input("Enter hub name: ")
        if hub_name not in self.hubs:
            print("Hub does not exist")
            return

        print("1. Electric Car")
        print("2. Electric Scooter")
        choice = input("Choose vehicle type: ")

        vehicle_id = int(input("Enter vehicle ID: "))
        model = input("Enter model name: ")
        battery = int(input("Enter battery percentage: "))

        if choice == "1":
            seats = int(input("Enter seating capacity: "))
            vehicle = ElectricCar(vehicle_id, model, battery, seats)
        elif choice == "2":
            speed = int(input("Enter max speed: "))
            vehicle = ElectricScooter(vehicle_id, model, battery, speed)
        else:
            print("Invalid option")
            return

        self.hubs[hub_name].append(vehicle)
        print("Vehicle added successfully")

    def display_hub_vehicles(self):
        hub_name = input("Enter hub name: ")
        if hub_name in self.hubs:
            distance = float(input("Enter trip distance: "))
            for v in self.hubs[hub_name]:
                v.display()
                print("Trip Cost:", v.calculate_trip_cost(distance))
                print("-" * 30)
        else:
            print("Hub not found")

    def main(self):
        while True:
            print("\n1. Add Hub")
            print("2. Add Vehicle to Hub")
            print("3. Display Hub Vehicles")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_hub()
            elif choice == "2":
                self.add_vehicle_to_hub()
            elif choice == "3":
                self.display_hub_vehicles()
            elif choice == "4":
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    ecorideobj= EcoRideMain()
    ecorideobj.display()
    ecorideobj.main()
