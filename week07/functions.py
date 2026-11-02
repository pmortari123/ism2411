# ISM2411 - Python for Business
# ===================== SELF-ASSESSMENT =====================
# Q1. First bug spotted in Exercise 5:
#   The first bug I hit was the missing colon on the second for loop
#   ("for sale in sales"). Python refuses to run the file at all and the
#   traceback (SyntaxError: expected ':') points right at that line, so I
#   found it from the traceback. The second bug (total = sale instead of
#   total += sale) gave no error at all - I only caught it by adding a
#   print() inside the loop and seeing total just jump to each sale instead
#   of growing, then confirmed it by explaining the loop out loud. The third
#   bug (while i <= len(sales)) raised IndexError: list index out of range,
#   which the traceback pointed to, and saying "i goes up to 5, but the last
#   index is 4" out loud made it obvious. Takeaway: tracebacks find crashes
#   fast, but logic bugs that don't crash need print() and slow reading.
#
# Q2. apply_discount(price, tier) in plain English:
#   It takes a price (a number) and a customer tier (a string: "gold",
#   "silver", "bronze", or anything else). It returns the price after the
#   tier's discount: gold 15% off, silver 10% off, bronze 5% off, and any
#   other tier gets no discount. Yes - a colleague could use it just from
#   the name, the inputs, and the docstring without reading the body.
#
# Q3. AI disclosure:
#   AI used: Claude (Anthropic) was used to help write and check the code
#   in this file and to draft these comments. I reviewed every line, ran
#   the script, and confirmed the outputs match the lab's expected output.
# ===========================================================


# --- Exercise 1 ---
def calculate_tax(price, rate):
    """Return the tax owed on price at the given rate (e.g. 0.07 for 7%)."""
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    """Return price after the tier discount: gold 15%, silver 10%, bronze 5%, else 0%."""
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0.0
    return price * (1 - discount)


for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")


# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
after_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${after_tax:.2f}")


def final_price(price, tier, tax_rate):
    """Apply the tier discount, then add tax, and return the final price."""
    discounted_price = apply_discount(price, tier)
    return discounted_price + calculate_tax(discounted_price, tax_rate)


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
# Fixed version of broken_sales.py
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    # Bug 1 fix: "total = sale" overwrote total each time, so it ended as the
    # last sale (90). Using += adds each sale to the running total instead.
    total += sale
print(f"Total: ${total}")

count = 0
# Bug 2 fix: the for statement was missing its colon at the end, which is a
# SyntaxError - Python needs ":" to start the loop body.
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
# Bug 3 fix: "i <= len(sales)" let i reach 5, but the last valid index is 4,
# causing IndexError: list index out of range. Using < stops at the last item.
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
x = 100  # global variable


def double_it():
    x = 999  # local variable - different from global x!
    return x * 2


print(x)            # prints 100
print(double_it())  # prints 1998
print(x)            # still prints 100 - x has not changed

# Scope explanation:
# A variable created inside a function is "local" - it only exists while the
# function runs. The x = 999 inside double_it() is a brand-new local x that
# just happens to share a name with the global x. Assigning to it doesn't
# touch the global x, so double_it() returns 999 * 2 = 1998, but the global
# x outside the function stays 100 before and after the call.