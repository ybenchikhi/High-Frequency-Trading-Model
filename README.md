# High-Frequency-Trading-Model
This is a C++ implementation of a high frequency trading model, designed to minimize latency and take advantage of market inefficiencies to maximize profits. The model uses the FIX protocol to receive real-time market data and make trading decisions based on the updated OrderBook.

Requirements
A compiler that supports C++11 or later
A market data provider that supports the FIX protocol
Getting Started:
Clone the repository to your local machine:

Establish a FIX connection with your market data provider and subscribe to the symbols you are interested in receiving market data for.

Implementation Details
The model consists of several key components:

OrderBook class: Keeps track of the bid and ask prices for each symbol, as well as the trade volume.
Market data subscription and parsing: Subscribes to real-time market data using the FIX protocol and parses the received messages to extract the relevant information.
Trading decision: Makes a trading decision based on the updated OrderBook.
Limitations
This implementation is intended for educational and demonstration purposes only and may not be suitable for real-world trading. Before using this model, it is important to understand the risks associated with high frequency trading and to thoroughly test and validate the model in a simulated trading environment.

Contributing
If you'd like to contribute to this project, please open a pull request or an issue on the GitHub repository.

License
This project is licensed under the MIT License. 
