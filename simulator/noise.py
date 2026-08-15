import numpy as np

def inject_fault(readings, threshold):
    n_readings = len(readings)
    faulted = []
    labels = []
    threshold_count = 0

    for i in range(n_readings):
        if i >= threshold * n_readings:
            threshold_count += 1
            step = 1 + (0.1 * threshold_count)
            faulted.append(round(readings[i] + step, 2))
            labels.append("fault")
        else:
            faulted.append(round(readings[i], 2))
            labels.append("normal")

    return(faulted, labels)
