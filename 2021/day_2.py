
file1 = open('day_2_input.txt', 'r')
Lines = file1.readlines()

pos_x = 0
pos_y = 0

for line in Lines:
    direction, value = line.strip().split()
    value = int(value)
    if direction == "forward":
        pos_x += value
    if direction == "down":
        pos_y += value
    if direction == "up":
        pos_y -= value

print("Total forward : {}, down: {}, combined: {}".format(
    pos_x, pos_y, pos_x * pos_y))


pos_x = 0
pos_y = 0
aim = 0
for line in Lines:
    direction, value = line.strip().split()
    value = int(value)
    if direction == "forward":
        pos_x += value
        pos_y += value * aim
    if direction == "down":
        aim += value
    if direction == "up":
        aim -= value

print("part 2 : Total forward : {}, down: {}, combined: {}".format(
    pos_x, pos_y, pos_x * pos_y))
