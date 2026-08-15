from simulator.sensor import Sensor
from simulator.noise import inject_fault

sensor = Sensor(sensor_type="temp", baseline=20, noise_std=0.5)
clean = sensor.generate_stream(n_readings=100)
faulted, labels = inject_fault(clean, threshold=0.7)

print(faulted, labels)