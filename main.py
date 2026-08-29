import pandas as pd
from simulator.sensor import Sensor
from simulator.noise import inject_fault
from analysis.stats import save_to_csv
from analysis.visualize import plot_readings
from models.classifier import load_and_prepare, train_and_evaluate
from data.generate_dataset import generate_dataset

sensor = Sensor(sensor_type="temp", baseline=20, noise_std=0.5)
clean = sensor.generate_stream(n_readings=100)
faulted, labels = inject_fault(clean, threshold=0.7)
save_to_csv(faulted, labels)

# Create different train and test splits to prevent overfitting
X_train, X_test, y_train, y_test = load_and_prepare("sensor_readings.csv")
model, predictions = train_and_evaluate(X_train, X_test, y_train, y_test)

df = pd.read_csv("sensor_readings.csv")
plot_readings(df)

print(generate_dataset(num_sequences=500, sequence_length=100))