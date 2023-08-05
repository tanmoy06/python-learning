try:
    age = int(input('Age: '))
    income = 10000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age can not be zero.')
