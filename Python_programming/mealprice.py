child_meal_price = float(input("Enter the price of a child's meal: $"))
adult_meal_price = float(input("Enter the price of an adult's meal: $"))
num_children = int(input("Enter the number of children: "))
num_adults = int(input("Enter the number of adults: "))
sales_tax_rate = float(input("Enter the sales tax rate (as a percentage): "))

# Calculate the subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
print(f"\nSubtotal: ${subtotal:.2f}")

# Calculate the sales tax
sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales tax: ${sales_tax:.2f}")

# Calculate the total price
total_price = subtotal + sales_tax
print(f"Total price: ${total_price:.2f}")

# Ask for payment amount
payment_amount = float(input("\nEnter the payment amount: $"))

# Calculate the change
change = payment_amount - total_price
print(f"Change: ${change:.2f}")