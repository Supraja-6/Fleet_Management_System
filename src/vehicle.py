class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = battery_percentage
        self.__maintenance_status = "Available"

    def get_battery_percentage(self):
        return self.__battery_percentage

    def get_maintenance_status(self):
        return self.__maintenance_status
    
    def set_battery_percentage(self, value):
        if 0 <= value <= 100:
            self.__battery_percentage = value
        else:
            raise ValueError("Battery percentage must be between 0 and 100")

    def set_maintenance_status(self, status):
        allowed = ["Available", "On Trip", "Under Maintenance"]
        if status in allowed:
            self.__maintenance_status = status
        else:
            raise ValueError("Invalid maintenance status")

    def display(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Model: {self.model}")
        print(f"Battery: {self.__battery_percentage}%")
        print(f"Status: {self.__maintenance_status}")
