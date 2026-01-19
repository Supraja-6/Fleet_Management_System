from battery_analytics import classify_battery_ranges

def test_classify_battery_ranges():
    rows = [
        {"battery": "5"},
        {"battery": "25"},
        {"battery": "85"},
        {"battery": "95"}
    ]

    result = classify_battery_ranges(rows)

    assert len(result["0-10"]) == 1
    assert len(result["20-30"]) == 1
    assert len(result["80-90"]) == 1
    assert len(result["90-100"]) == 1
