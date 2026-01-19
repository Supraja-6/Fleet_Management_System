import csv
import json

def classify_battery_ranges(rows):
    battery_ranges = {
        "0-10": [],
        "10-20": [],
        "20-30": [],
        "30-40": [],
        "40-50": [],
        "50-60": [],
        "60-70": [],
        "70-80": [],
        "80-90": [],
        "90-100": []
    }

    for row in rows:
        battery = int(row["battery"])

        if 0 <= battery < 10:
            battery_ranges["0-10"].append(row)
        elif battery < 20:
            battery_ranges["10-20"].append(row)
        elif battery < 30:
            battery_ranges["20-30"].append(row)
        elif battery < 40:
            battery_ranges["30-40"].append(row)
        elif battery < 50:
            battery_ranges["40-50"].append(row)
        elif battery < 60:
            battery_ranges["50-60"].append(row)
        elif battery < 70:
            battery_ranges["60-70"].append(row)
        elif battery < 80:
            battery_ranges["70-80"].append(row)
        elif battery < 90:
            battery_ranges["80-90"].append(row)
        else:
            battery_ranges["90-100"].append(row)

    return battery_ranges


def read_fleet_csv(file_path):
    with open(file_path, "r") as file:
        return list(csv.DictReader(file))


def write_output_json(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
