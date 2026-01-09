from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    def __init__(self):
        self.hubs = {}  

    def display(self):
        print("Welcome to Eco-Ride Urban Mobility System")

    def add_hub(self):
        hub_name = input("Enter hub name: ").strip().title()
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' added successfully")
        else:
            print("Hub already exists")

    def add_vehicle_to_hub(self):
        hub_name = input("Enter hub name: ").strip().title()
        if hub_name not in self.hubs:
            print("Hub does not exist")
            return
        
        while True:
            v_type = input("Enter vehicle type (Car/Scooter): ").strip().lower()
            if v_type in ["car", "scooter"]:
                break
            print("Invalid input! Please enter 'Car' or 'Scooter'")

        try:
            vehicle_id = int(input("Enter vehicle ID: "))
        except ValueError:
            print("Vehicle ID must be number")
            return
        
        if any(v.vehicle_id == vehicle_id for v in self.hubs[hub_name]):
            print(f"Vehicle ID {vehicle_id} already exists in {hub_name}")
            return

        model = input("Enter model name: ").strip()
        while True:
            try:
                battery = int(input("Enter battery percentage: "))
                if 0 <= battery <= 100:
                    break
                print("Battery must be 0-100")
            except ValueError:
                print("Enter a valid number")

        if v_type == "car":
            seats = int(input("Enter seating capacity: "))
            vehicle = ElectricCar(vehicle_id, model, battery, seats)
        elif v_type == "scooter":
            speed = int(input("Enter max speed limit: "))
            vehicle = ElectricScooter(vehicle_id, model, battery, speed)
        else:
            print("Incalid vehicle type")
            return
        

        self.hubs[hub_name].append(vehicle)
        print("Vehicle added successfully")

    def display_hub_vehicles(self):
        hub_name = input("Enter hub name: ").strip().title()
        if hub_name not in self.hubs:
            print("Hub not found")
            return

        print(f"\nVehicles in {hub_name} Hub")
        for v in self.hubs[hub_name]:
            v.display()
            while True:
                try:
                    value = float(input("Enter trip distance/minutes: "))
                    if value < 0:
                        print("Value cannot be negative")
                        continue
                    break
                except ValueError:
                    print("enter a valid number")
            print("Trip Cost:", v.calculate_trip_cost(value))
            print("-" * 30)


    def search_by_hub(self):
        hub_name = input("Enter hub name to search vehicles: ").strip().title()
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
            high_battery_vehicles = [v for v in vehicles if v.get_battery_percentage() > threshold]
            if high_battery_vehicles:
                found = True
                print(f"\nHub: {hub_name}")
                for v in high_battery_vehicles:
                    v.display()
                    print("-" * 30)
        if not found:
            print("No vehicles found with battery > 80%")

    def categorized_view(self):
        print("\n--- Categorized Vehicle View ---")
        cars = []
        scooters = []
        for vehicles in self.hubs.values():
            for v in vehicles:
                if isinstance(v, ElectricCar):
                    cars.append(v)
                elif isinstance(v, ElectricScooter):
                    scooters.append(v)
        print("\nElectric Cars: ")
        if cars:
            for car in cars:
                car.display()
                print("-" * 30)
        else:
            print("No Electric Cars available")

        print("\nElectric Scooters: ")
        if scooters:
            for scooter in scooters:
                scooter.display()
                print("-" * 30)
        else:
            print("No Electric Scooters available")

    def fleet_analytics(self):
        print("\n--- Fleet Analytics (Status Summary)---")
        available = 0
        on_trip = 0
        under_maintenance = 0
        for vehicles in self.hubs.values():
            for v in vehicles:
                status = v.get_maintenance_status()
                if status == "Available":
                    available += 1
                elif status == "On Trip":
                    on_trip += 1
                elif status == "Under Maintenance":
                    under_maintenance += 1
        total = available + on_trip + under_maintenance
        if total == 0:
            print("No vehicles available")
            return
        print(f"Total Vehicles         : {total}")
        print(f"Available              : {available}")
        print(f"On Trip                : {on_trip}")
        print(f"Under Maintenance      : {under_maintenance}")

    def sort_vehicles_by_model(self):
        hub_name = input("Enter hub name to sort vehicles: ").strip().title()
        if hub_name not in self.hubs:
            print("Hub not found")
            return

        if not self.hubs[hub_name]:
            print(f"No vehicles in hub '{hub_name}'")
            return

        self.hubs[hub_name].sort(key=lambda v: v.model.lower())

        print(f"\nVehicles in hub '{hub_name}' sorted alphabetically by Model:")
        for v in self.hubs[hub_name]:
            print(v) 
            print("-" * 30)

    
    def main(self):
        while True:
            print("\n--- MENU ---")
            print("1. Add Hub")
            print("2. Add Vehicle to Hub")
            print("3. Display Hub Vehicles")
            print("4. Search Vehicles by Hub")
            print("5. Search Vehicles with Battery > 80%")
            print("6. Categorized View (Cars/Scooters)")
            print("7. Fleet Analytics (Status)")
            print("8. Sort Vehicles Alphabetically by Model")
            print("9. Exit")


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
                self.categorized_view()
            elif choice == "7":
                self.fleet_analytics()
            elif choice == "8":
                self.sort_vehicles_by_model()
            elif choice == "9":
                print("Exiting system")
                break
            else:
                print("Invalid option")


if __name__ == "__main__":
    ecorideobj = EcoRideMain()
    ecorideobj.display()
    ecorideobj.main()
