class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage
    def display(self):
        print(f"vehicle_id : {self.vehicle_id} model: {self.model} battery_percentage : {self.battery_percentage}")
