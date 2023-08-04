for item in 'Python':
    print(item, end=" ")
print("\n")
for i in range(1,11):
    print(i, end = " ")
print("\n")
for i in range(1,11,2):
    print(i, end = " ")

# sum

prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")