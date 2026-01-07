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

        if any(v.vehicle_id == vehicle_id for v in self.hubs[hub_name]):
            print(f"Vehicle ID {vehicle_id} already exists in {hub_name}")
            return

        model = input("Enter model name: ")
        battery = int(input("Enter battery percentage: "))

        if choice == "1":
            seats = int(input("Enter seating capacity: "))
            vehicle = ElectricCar(vehicle_id, model, battery, seats)
        elif choice == "2":
            speed = int(input("Enter max speed: "))
            vehicle = ElectricScooter(vehicle_id, model, battery, speed)
        else:
            print("Invalid choice")
            return

        self.hubs[hub_name].append(vehicle)
        print("Vehicle added successfully")

    def display_hub_vehicles(self):
        hub_name = input("Enter hub name: ")
        if hub_name not in self.hubs:
            print("Hub not found")
            return

        distance = float(input("Enter trip distance: "))
        print(f"\nVehicles in {hub_name} Hub")
        for v in self.hubs[hub_name]:
            v.display()
            print("Trip Cost:", v.calculate_trip_cost(distance))
            print("-" * 30)

    def search_by_hub(self):
        hub_name = input("Enter hub name to search vehicles: ")
        if hub_name not in self.hubs:
            print("Hub not found")
            return

        print(f"\nVehicles in hub '{hub_name}':")
        for v in self.hubs[hub_name]:
            v.display()
            print("-" * 30)

    def search_high_battery(self):
        threshold = 80
        found = False
        print("\nVehicles with battery > 80%:")
        for hub_name, vehicles in self.hubs.items():
            high_battery_vehicles = list(filter(lambda v: v.get_battery_percentage() > threshold, vehicles))
            if high_battery_vehicles:
                found = True
                print(f"\nHub: {hub_name}")
                for v in high_battery_vehicles:
                    v.display()
                    print("-" * 30)
        if not found:
            print("No vehicles found with battery > 80%")

    def main(self):
        while True:
            print("\n--- MENU ---")
            print("1. Add Hub")
            print("2. Add Vehicle to Hub")
            print("3. Display Hub Vehicles")
            print("4. Search Vehicles by Hub")
            print("5. Search Vehicles with Battery > 80%")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_hub()
            elif choice == "2":
                self.add_vehicle_to_hub()
            elif choice == "3":
                self.display_hub_vehicles()
            elif choice == "4":
                self.search_by_hub()
            elif choice == "5":
                self.search_high_battery()
            elif choice == "6":
                print("Exiting system")
                break
            else:
                print("Invalid option")


if __name__ == "__main__":
    ecorideobj = EcoRideMain()
    ecorideobj.display()
    ecorideobj.main()
