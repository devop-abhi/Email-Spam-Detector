import pandas as pd

# Load the dataset
data = pd.read_csv(
    "SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Display the first five messages
print(data.head())

# Display the dataset size
print("\nDataset shape:", data.shape)

# Count spam and legitimate messages
print("\nMessage distribution:")
print(data["label"].value_counts())