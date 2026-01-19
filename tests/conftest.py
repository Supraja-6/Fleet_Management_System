import sys
import os

# Add src folder to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import pytest
from Ecoride_main import EcoRideMain
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


@pytest.fixture
def ecoride():
    eco = EcoRideMain()
    eco.hubs = {
        "Bangalore": [
            ElectricCar(1, "Tesla", 90, 5),
            ElectricScooter(2, "Ola", 60, 60),
            ElectricCar(3, "BMW", 85, 4),
        ],
        "Hyderabad": []
    }
    return eco
