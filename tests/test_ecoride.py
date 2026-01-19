from Ecoride_main import EcoRideMain
from electric_car import ElectricCar
from electric_scooter import ElectricScooter

def setup_ecoride():
    eco = EcoRideMain()
    eco.hubs["Bangalore"] = [
        ElectricCar(1, "Tesla", 90, 5),
        ElectricScooter(2, "Ola", 70, 60),
        ElectricCar(3, "BMW", 85, 4)
    ]
    return eco

def test_search_high_battery():
    eco = setup_ecoride()
    high_battery = [
        v for v in eco.hubs["Bangalore"]
        if v.get_battery_percentage() > 80
    ]
    assert len(high_battery) == 2

def test_sort_vehicles_by_model():
    eco = setup_ecoride()
    eco.hubs["Bangalore"].sort(key=lambda v: v.model.lower())
    models = [v.model for v in eco.hubs["Bangalore"]]
    assert models == ["BMW", "Ola", "Tesla"]

def test_fleet_analytics_counts():
    eco = setup_ecoride()
    available = sum(
        1 for v in eco.hubs["Bangalore"]
        if v.get_maintenance_status() == "Available"
    )
    assert available == 3
