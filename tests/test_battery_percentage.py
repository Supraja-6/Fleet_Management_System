import pytest
from electric_car import ElectricCar

@pytest.mark.parametrize(
    "battery",
    [0, 10, 50, 100]
)
def test_valid_battery_percentage(battery):
    car = ElectricCar(1, "Tesla", battery, 5)
    assert car.get_battery_percentage() == battery


@pytest.mark.parametrize(
    "battery",
    [-1, 101, 150]
)
def test_invalid_battery_percentage(battery):
    with pytest.raises(ValueError):
        ElectricCar(2, "BMW", battery, 4)
