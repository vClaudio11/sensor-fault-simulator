from simulator.sensor import Sensor
from simulator.noise import inject_fault
from analysis.stats import save_to_csv

sensor = Sensor(sensor_type="temp", baseline=20, noise_std=0.5)
clean = sensor.generate_stream(n_readings=100)
faulted, labels = inject_fault(clean, threshold=0.7)
to_csv = save_to_csv(faulted, labels)

print(faulted, labels)