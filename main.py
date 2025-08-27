def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If discount is 20% or higher, apply it; otherwise return original price.
    """
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price


# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)

    # Print result
    if discount_percent >= 20:
        print(f"Discount applied! Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Original price: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numbers.")
