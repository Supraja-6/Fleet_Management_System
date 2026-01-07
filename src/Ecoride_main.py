from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class EcoRideMain:
    def display(self):
        print("Welcome to Eco-Ride Urban Mobility System")

    def main(self):
        car = ElectricCar(101, "Tesla", 90, 5)
        scooter = ElectricScooter(102, "Honda", 80, 60)

        car.display()
        print("-" * 30)
        scooter.display()

if __name__ == "__main__":
    ecorideobj = EcoRideMain()
    ecorideobj.display()
    ecorideobj.main()
