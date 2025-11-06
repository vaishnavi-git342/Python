def calculate():
    age = int(input("Enter your age: "))
    p = int(input("Enter the principal amount: "))
    n = int(input("Enter the number of years: "))

    if age < 60:
        r = 10
    else:
        r = 12

    print("Rate of interest:", r)

    s = (p * n * r) / 100
    print("Simple Interest =", s)

calculate()
