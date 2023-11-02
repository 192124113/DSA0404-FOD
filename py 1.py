item_prices = [10, 5, 3, 8]  
quantities = [2, 3, 5, 1]     
discount_rate = 10
tax_rate = 8
total_cost_before_discount = sum(item_price * quantity for item_price, quantity in zip(item_prices, quantities))
discount_amount = (discount_rate / 100) * total_cost_before_discount
total_cost_after_discount = total_cost_before_discount - discount_amount
tax_amount = (tax_rate / 100) * total_cost_after_discount
final_total_cost = total_cost_after_discount + tax_amount
print(f"Total cost of the purchase, including discounts and taxes: ${final_total_cost:.2f}")
