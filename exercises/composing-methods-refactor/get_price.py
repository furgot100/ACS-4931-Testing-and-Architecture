# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.
base_price = quantity * item_price
discount_factor = 0
def get_price(base_price, discount_factor):
    if base_price > 1000:
        discount_factor = 0.95
    else:
        discount_factor = 0.98
    return base_price * discount_factor

price = get_price(base_price, discount_factor)
