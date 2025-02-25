#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.prices = []
        self.items = []
        
    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)
        self.prices.extend([price] * quantity)
        items_total = price * quantity
        self.total = self.total + items_total

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total - self.total * self.discount / 100
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.total:
          last_item = self.prices[-1]
          count = self.prices.count(last_item)
          self.total -= last_item * count
          self.items.pop()
          for _ in range(count):
            self.prices.pop()
            self.items.pop()
        else:
            return "0.0"