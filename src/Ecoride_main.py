from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    def display(self):
        print("Welcome to Eco-Ride Urban Mobility System")

    def main(self):
        car = ElectricCar(101, "Tesla", 90, 5)
        scooter = ElectricScooter(102, "Honda", 80, 60)

        vehicles = [car, scooter]
        for v in vehicles:
            v.display()
            print("Trip Cost for 10 units: ", v.calculate_trip_cost(10))
            print("-" * 30)

if __name__ == "__main__":
    ecorideobj = EcoRideMain()
    ecorideobj.display()
    ecorideobj.main()
