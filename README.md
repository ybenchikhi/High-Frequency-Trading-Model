This project is aimed at creating a high frequency trading model to buy and sell stocks with the highest potential for profit. The model consists of two parts: a Convolutional Neural Network (CNN) trained to make predictions based on the stock's historical volatility, and a C++ file that executes the trades with ultra low latency.

Requirements:
TensorFlow,
Numpy,
Pandas,
yfinance.
Data Processing:
The data for the stocks is obtained from Yahoo Finance using the yfinance library. The data is preprocessed to calculate the stock's volatility over the past 5 minutes and is used as the input to the CNN.

Convolutional Neural Network:
The CNN model is a binary classification model trained to predict if a stock will make a profit in the next 5 minutes based on its volatility over the past 5 minutes. The model consists of 4 dense layers with increasing numbers of neurons and uses a sigmoid activation function in the output layer to produce binary predictions. The model has been pre-trained and the weights are stored in model_weights.h5.

Trading Execution:
The trades are executed using a C++ file that implements a low latency trading algorithm. The file takes the ticker symbol of the stock as input and executes a buy or sell order accordingly. The CNN model and the C++ file are integrated in a Python script that calls the C++ file for each stock in a list of stock tickers if the CNN predicts a high enough return.

Usage
Clone the repository: git clone
Install the required libraries: pip install -r requirements.txt
Run the trading script: python trade.py
Note:
This is only a sample project and has yet to be tested with real-time data only historical data.
