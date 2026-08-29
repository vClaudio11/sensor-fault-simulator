import numpy as np
from simulator.sensor import Sensor
from simulator.noise import inject_fault
import random

def generate_dataset(num_sequences, sequence_length):
    all_sequences = []
    all_labels = []

    for _ in range(num_sequences):
        sensor = Sensor(sensor_type="temp", baseline=20, noise_std=0.5)
        clean = sensor.generate_stream(n_readings=sequence_length)

        has_fault = random.choice([True, False])
        if has_fault:
            threshold = random.uniform(0.3, 0.9) # Randomized fault start position
            faulted, _ = inject_fault(clean, threshold=threshold)
            all_sequences.append(faulted)
            all_labels.append(1)
        else:
            all_sequences.append(clean)
            all_labels.append(0)

    return np.array(all_sequences) , np.array(all_labels)