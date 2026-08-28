import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

# pd.read_csv allows us to read the heading names of the csv file and classify the columns
def load_and_prepare(csv_path):
    df = pd.read_csv(csv_path)
    X = df[["Readings"]]
    y = df["Status"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model, strictly fit only training data, predict only test data
def train_and_evaluate(X_train, X_test, y_train, y_test):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    # Output the precision, recall and F1 score of the predictions
    print(confusion_matrix(y_test, predictions, labels=["fault", "normal"]))
    print("Precision:", precision_score(y_test, predictions, pos_label="fault"))
    print("Recall:", recall_score(y_test, predictions, pos_label="fault"))
    print("F1:", f1_score(y_test, predictions, pos_label="fault"))
    return model, predictions