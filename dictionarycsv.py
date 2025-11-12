import csv

field_name = ['NO', 'company', 'car model']
car = [
    {'NO': 1, 'company': 'Ferrari', 'car model': 'GH'},
    {'NO': 2, 'company': 'BMW', 'car model': 'X5'},
    {'NO': 3, 'company': 'maruthi suzuki', 'car model': 'Swift'},
    {'NO': 4, 'company': 'Audi', 'car model': 'Rs7'},
    {'NO': 5, 'company': 'Toyota', 'car model': 'Fortuner'},
]

# Writing to CSV
with open('car.csv', 'w', newline='') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=field_name)
    write.writeheader()
    write.writerows(car)

# Reading from CSV
with open('car.csv', newline='') as csvfile:
    d = csv.reader(csvfile)
    for r in d:
        print(', '.join(r))  
