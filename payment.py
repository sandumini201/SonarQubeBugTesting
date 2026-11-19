
def process_payment(amount, card_number):
    if amount > 0:
        print("Payment successful")
    else:
        print("Invalid amount")

    return True

def calculate_discount(price):
    discount = price * 0.10
    return price - discount

def divide_payment(amount, people):
    return amount / people

