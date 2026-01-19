def test_sort_by_battery(ecoride):
    vehicles = ecoride.hubs["Bangalore"]
    sorted_vehicles = sorted(
        vehicles,
        key=lambda v: v.get_battery_percentage(),
        reverse=True
    )

    batteries = [v.get_battery_percentage() for v in sorted_vehicles]
    assert batteries == sorted(batteries, reverse=True)
