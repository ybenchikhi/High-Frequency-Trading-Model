#include <iostream>
#include <unordered_map>
#include <chrono>
#include <thread>
#include <vector>
#include <mutex>
#include <condition_variable>

using namespace std;
using namespace std::chrono;

class OrderBook {
 public:
  // Add an order to the book
  void addOrder(string symbol, double price, int size) {
    order_book_[symbol][price].size += size;
  }

  // Remove an order from the book
  void removeOrder(string symbol, double price, int size) {
    order_book_[symbol][price].size -= size;

    // If the size of the order at this price is 0, remove it
    if (order_book_[symbol][price].size == 0) {
      order_book_[symbol].erase(price);
    }

    // If there are no orders for this symbol, remove it from the book
    if (order_book_[symbol].empty()) {
      order_book_.erase(symbol);
    }
  }

  // Return the best bid for a symbol
  pair<double, int> bestBid(string symbol) {
    if (order_book_.count(symbol) == 0) {
      return make_pair(-1.0, 0);
    }
    return make_pair(order_book_[symbol].rbegin()->first, order_book_[symbol].rbegin()->second.size);
  }

