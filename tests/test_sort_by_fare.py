def test_sort_by_fare(ecoride):
    distance = 10
    vehicles = ecoride.hubs["Bangalore"]

    sorted_vehicles = sorted(
        vehicles,
        key=lambda v: v.calculate_trip_cost(distance),
        reverse=True
    )

    fares = [v.calculate_trip_cost(distance) for v in sorted_vehicles]
    assert fares == sorted(fares, reverse=True)
