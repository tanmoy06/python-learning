customer = {
    "name": "Tanmoy Sarkar",
    "age": 20,
    "is_verified": True
}
print(customer["name"])
customer["name"] = "Muntasir Sayan"
print(customer["name"])

phone_number = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three"
}
output = ""
for ch in phone_number:
    output += digits_mapping.get(ch, "!") + " "
print(output)