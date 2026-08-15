import numpy as np

class Sensor:
    def __init__(self, sensor_type, baseline, noise_std):
        self.sensor_type = sensor_type
        self.baseline = baseline
        self.noise_std = noise_std

    def generate_stream(self, n_readings):
        readings = []
        for i in range(n_readings):
            reading = np.random.normal(self.baseline, self.noise_std)
            readings.append(reading)
        return readings