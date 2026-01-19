from battery_analytics import (
    read_fleet_csv,
    classify_battery_ranges,
    write_output_json
)

if __name__ == "__main__":
    rows = read_fleet_csv("fleet_data.csv")
    result = classify_battery_ranges(rows)
    write_output_json(result, "output.json")
