def cart_total(prices, discount=0):
  total = sum(prices)
  final_price = total * (1 - discount / 100)
  return final_price

print(cart_total([10, 20, 30]))
print(cart_total([10, 20, 30], discount=10)) 