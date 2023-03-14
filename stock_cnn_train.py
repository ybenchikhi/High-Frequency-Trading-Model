import tensorflow as tf
import numpy as np
import pandas as pd
import yfinance as yf
import subprocess

# Define a function to download and preprocess data for a given stock
def get_data(ticker):
    df = yf.download(ticker, period="1m", interval="1m")
    volatility = df['Close'].rolling(5).std()
    X = np.array(volatility[-6:-1]).reshape(1, -1)
    return X, 1 if df['Close'][-1] > df['Open'][-1] else 0 # label as 1 if close price > open price else 0

# Load the pre-trained model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(5, )),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model using online learning
while True:
    # Define a list of stock tickers to check
    tickers = ["AAPL", "GOOG", "MSFT", "TSLA", "AMZN"]

    # Iterate over the list of tickers
    for ticker in tickers:
        X, y = get_data(ticker)
        loss, accuracy = model.train_on_batch(X, y)

        if accuracy > 0.5:
            subprocess.call(["./ultra_low_latency_trading_model", ticker])
            print("Bought stock", ticker, "- Loss:", loss, "- Accuracy:", accuracy)
        else:
            print("Not buying stock", ticker, "- Loss:", loss, "- Accuracy:", accuracy)
