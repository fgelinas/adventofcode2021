# Running the advent of code 2021 in python
# https://adventofcode.com/2021/day/1
# François Gélinas

file1 = open('day_1_input.txt', 'r')
Lines = file1.readlines()

prev_value = int(Lines.pop(0).strip())
nb_increment = 0
for line in Lines:
    new_value = int(line.strip())
    if (new_value > prev_value):
        nb_increment += 1
        print("{} is > {} -- nb increment : {}".format(new_value,
              prev_value, nb_increment))

    else:
        print("{} is < {}".format(new_value, prev_value))
    prev_value = new_value

print("nb increments : {}".format(nb_increment))
