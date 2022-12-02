# Running the advent of code 2021 in python
# https://adventofcode.com/2021/day/1
# François Gélinas

file1 = open('day_1_input.txt', 'r')
Lines = file1.readlines()

nb_increment = 0
for i in range(1, len(Lines)):
    if int(Lines[i].strip()) > int(Lines[i-1].strip()):
        nb_increment += 1
        # print("comparing value {} to {}".format(
        #    int(Lines[i].strip()), int(Lines[i-1].strip())))

print("nb increments : {}".format(nb_increment))

nb_increment = 0
for i in range(3, len(Lines)):
    if int(Lines[i].strip()) > int(Lines[i-3].strip()):
        nb_increment += 1
        # print("comparing value {} to {}".format(
        #    int(Lines[i].strip()), int(Lines[i-3].strip())))


print("nb new increments : {}".format(nb_increment))
