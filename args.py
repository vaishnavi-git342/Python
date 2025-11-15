def add(*args):
    total = 0
    for i in args:
        total += i
    print("sum is", total)
    return total   # you need a return value

# get user input OUTSIDE the function
input_numbers = input("enter integers separated by spaces: ").split()
input_numbers = [int(num) for num in input_numbers]

result = add(*input_numbers)
