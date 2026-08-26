from simulator.sensor import Sensor
from simulator.noise import inject_fault
from analysis.stats import save_to_csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

sensor = Sensor(sensor_type="temp", baseline=20, noise_std=0.5)
clean = sensor.generate_stream(n_readings=100)
faulted, labels = inject_fault(clean, threshold=0.7)
to_csv = save_to_csv(faulted, labels)

# pd.read_csv allows us to read the heading names of the csv file and classify the columns
df = pd.read_csv("sensor_readings.csv")
X = df[["Readings"]]
y = df["Status"]

# Create different train and test splits to prevent overfitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Outputs the number of rows and features of X
print(X_train.shape)
print(X_test.shape)

# Define the model, strictly fit only training data, predict only test data
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions)
print(y_test.values)

print(confusion_matrix(y_test, predictions, labels=["fault", "normal"]))
print("Precision:", precision_score(y_test, predictions, pos_label="fault"))
print("Recall:", recall_score(y_test, predictions, pos_label="fault"))
print("F1:", f1_score(y_test, predictions, pos_label="fault"))

print(faulted, labels)