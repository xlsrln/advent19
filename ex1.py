from math import floor

# read list of modules
file = open("resources/ex1.csv", "r")
number_list = list(file)


# calculate fuel requirement per module
def fuel_calculation(x):
    return max(floor(int(x)/3, ) - 2, 0)


# calculate extra fuel recursively
def extra_fuel(x):
    fuel = fuel_calculation(x)
    if fuel == 0:
        return 0
    else:
        return fuel + extra_fuel(fuel)


# test values
print(fuel_calculation(1969) == 654)
print(fuel_calculation(100756) == 33583)

# test values part 2
print(extra_fuel(1969) == 966)
print(extra_fuel(100756) == 50346)

# first output
fuel_required = sum(map(fuel_calculation, number_list))
print(fuel_required)

# second output
total_extra_fuel = sum(map(extra_fuel, list(map(fuel_calculation, number_list))))
total_fuel = fuel_required + total_extra_fuel

print(total_fuel)

