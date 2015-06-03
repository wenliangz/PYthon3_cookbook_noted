# example.py
#
# Example of calculating with dictionaries


'''
Use zip() to invert the the dict into tuples that values come first. When performing comparisons on such tuples,
the value element is compared first, followed by the key. If the values are the same, go values.
'''

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('min price:', min_price)
print('max price:', max_price)

print('sorted prices:')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)


