import pytest
from electric_car import ElectricCar

@pytest.mark.parametrize(
    "status",
    ["Available", "On Trip", "Under Maintenance"]
)
def test_valid_maintenance_status(status):
    car = ElectricCar(1, "Tesla", 80, 5)
    car.set_maintenance_status(status)
    assert car.get_maintenance_status() == status


@pytest.mark.parametrize(
    "status",
    ["Broken", "Repair", "", None]
)
def test_invalid_maintenance_status(status):
    car = ElectricCar(2, "BMW", 70, 4)
    with pytest.raises(ValueError):
        car.set_maintenance_status(status)
