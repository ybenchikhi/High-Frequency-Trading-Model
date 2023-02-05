import numpy as np
import pandas as pd
import tensorflow as tf
from keras.layers import Conv1D, Dense, Flatten, MaxPooling1D
from keras.models import Sequential

# Load the stock price data into a Pandas DataFrame
df = pd.read_csv("stock_prices.csv")

# Preprocess the data by normalizing it
data = df.values
data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

# Split the data into training and testing sets
train_data = data[:int(0.8 * len(data))]
test_data = data[int(0.8 * len(data)):]

# Define the CNN model
model = Sequential([
    Conv1D(32, 5, activation='relu', input_shape=(len(df.columns), 1)),
    MaxPooling1D(2),
    Conv1D(64, 5, activation='relu'),
    MaxPooling1D(2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
train_data = np.expand_dims(train_data, axis=-1)
model.fit(train_data, train_labels, epochs=10)

# Evaluate the model on the test data
test_data = np.expand_dims(test_data, axis=-1)
test_loss, test_accuracy = model.evaluate(test_data, test_labels)
print("Test Accuracy:", test_accuracy)
