import csv

def save_to_csv(readings, labels):
    with open("sensor_readings.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Readings", "Status"])
        for reading, label in zip(readings, labels):
            writer.writerow([reading, label])