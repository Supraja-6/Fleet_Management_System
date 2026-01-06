from vehicle import Vehicle

class EcoRideMain:
    def display(self):
        print("Welcome to Eco-Ride Urban Mobility System")
    def main(self):
        v1 = Vehicle(101, "Tesla", 90, 1000)
        v1.display()
if __name__ == "__main__":
    ecoridemain = EcoRideMain()
    ecoridemain.display()