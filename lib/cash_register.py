#!/usr/bin/env python3


class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Discount must be an integer between 0 and 100.
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        # Add the cost of the items to the register total.
        self.total += price * quantity

        # Add each item to the items list based on its quantity.
        for _ in range(quantity):
            self.items.append(item)

        # Save the transaction so it can be voided later.
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }

        self.previous_transactions.append(transaction)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount

            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.previous_transactions:
            # Get and remove the most recent transaction.
            transaction = self.previous_transactions.pop()

            item = transaction["item"]
            price = transaction["price"]
            quantity = transaction["quantity"]

            # Subtract the transaction's cost from the total.
            self.total -= price * quantity

            # Remove the items from the items list.
            for _ in range(quantity):
                self.items.remove(item)