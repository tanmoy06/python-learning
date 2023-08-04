secret_number = 6
i = 0
while i < 3:
    number = int(input("Guess: "))
    i += 1
    if number == secret_number:
        print("You won !!")
        break
    else:
        continue
else:
    print("Sorry, you failed..")
