# Experiment 3: Configurable Payment Processing System
# Strategy Design Pattern - Advanced Python Programming Lab

from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Bitcoin.")


# Context Class
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


def main():
    amount = float(input("Enter payment amount: "))

    print("\nChoose Payment Method")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. Bitcoin")

    choice = input("Enter your choice: ")

    if choice == "1":
        strategy = CreditCardPayment()
    elif choice == "2":
        strategy = PayPalPayment()
    elif choice == "3":
        strategy = BitcoinPayment()
    else:
        print("Invalid Choice!")
        return

    processor = PaymentProcessor(strategy)
    print()
    processor.process_payment(amount)


if __name__ == "__main__":
    main()
