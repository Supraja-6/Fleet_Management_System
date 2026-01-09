from vehicle import Vehicle
class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        return 5 + (0.5 * distance)
    
    def __str__(self):
        return super().__str__() + f", Type: Electric Car, Seating Capacity: {self.seating_capacity}"

    def display(self):
        super().display()
        print(f"Type: Electric Car")
        print(f"Seating Capacity : {self.seating_capacity}")