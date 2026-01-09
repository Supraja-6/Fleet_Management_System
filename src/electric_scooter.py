from vehicle import Vehicle
class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, distance):
        return 1 + (0.15 * distance)
    
    def __str__(self):
        return super().__str__() + f", Type: Electric Scooter, Max Speed: {self.max_speed_limit} km/h"

    def display(self):
        super().display()
        print(f"Type: Electric Scooter")
        print(f"Max Speed: {self.max_speed_limit} km/h")
