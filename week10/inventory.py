# Reflection
# 1. What surprised me most about Python lists:
#    I was surprised that lists can be changed in place with methods like
#    .append(), .remove(), and .sort() without creating a new variable. Negative
#    indexing and slicing like [::2] also made it much easier to grab parts of a
#    list than I expected.
#
# 2. A real business situation where a list would have saved me time vs. Excel:
#    Over the summer I sold knives for a sales company and tracked my sales
#    from each appointment by hand. With a Python list of sale amounts I could
#    have used sum(), max(), and a filter loop to instantly get my weekly total,
#    my best sale, and which appointments went over a target. As a valet, a list
#    of ticket numbers would also make it quick to see which cars are still parked.

# Exercise 1: Build the list
print("--- Exercise 1 ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index practice
print("--- Exercise 2 ---")
print(inventory[0])                    # first item
print(inventory[-1])                   # last item
middle = len(inventory) // 2
print(inventory[middle])               # middle item

# Exercise 3: Slicing
print("--- Exercise 3 ---")
print(inventory[:3])                   # first three
print(inventory[-2:])                  # last two
print(inventory[::2])                  # every other item

# Exercise 4: Modify
print("--- Exercise 4 ---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5: Tuple comparison
print("--- Exercise 5 ---")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as e:
    print("TypeError caught:", e)
    print("Tuples are immutable, so coordinates can't be changed by accident.")
print(coords)

# Exercise 6: Average of a list of sales
print("--- Exercise 6 ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7: Accumulator pattern
print("--- Exercise 7 ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print("Original:", prices)
print("Discounted:", discounted)

# Exercise 8: Filter above threshold
print("--- Exercise 8 ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for s in sales:
    if s > 300:
        high_sales.append(s)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))