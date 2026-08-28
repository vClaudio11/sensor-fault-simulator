import matplotlib.pyplot as plt

# Plot readings line graph with mean average
def plot_readings(df):
    df.plot(y="Readings", figsize=(10,4))
    plt.axhline(y=df["Readings"].mean(), color="gray", linestyle="--")
    plt.show()