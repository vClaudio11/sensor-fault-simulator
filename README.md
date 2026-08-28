# Sensor Fault Simulator

A small pipeline that simulates sensor readings, injects a progressive fault into that data stream and trains and classifier to detect it.

## What it does
- Generates a clean sensor reading stream with realistic noise (`Sensor` class, `numpy`)
- Injects a progressive fault partway through the stream, with `normal`/`fault` labels (`inject_fault`)
- Saves the labeled data to CSV (`sensor_readings.csv`)
- Trains a logistic regression classifier to detect faults from readings, evaluated with precision, recall, and F1

## Scope
This is a personal learning project, built incrementally as I work through an ML/AI roadmap. It intentionally starts simple and grows in complexity:
- **Done:** simulate sensor data, inject a labeled fault, classify with logistic regression (precision/recall/F1)
- **In progress:** classify fault sequences with a 1D CNN (PyTorch)
- **Not yet started:** deployment / edge inference, real (non-simulated) sensor data

## Project structure
```
sensor_fault_simulator/
├── simulator/
│   └── noise.py - inject_fault() injects a progressive fault + labels
│   └── sensor.py - Sensor class, generates clean readings
├── analysis/
│   ├── stats.py - saves readings + labels as CSV
│   └── visualize.py - generates matplotlib graph for readings
├── models/
│   └── classifier.py - logistic regression model classifier
└── main.py - runs the full pipeline
```

## Setup
python -m venv venv
venv\Scripts\activate
pip install numpy pandas scikit-learn

## Run
python main.py

## Results
On a 100-row generated dataset with an 80/20 train/test split:
- Precision: 1.0
- Recall: 0.857
- F1: 0.923

## What I learned
- How to inject an incremental fault using np.random.normal using numpy
- How to read and classify data from csv columns using pandas
- The issue of overfitting and the need for separate train and test data
- Why accuracy needs to consist of recall, precision and F1 score
- Plotting line graphs using matplotlib to visualize sensor readings
