file1 = open('day_3_input.txt', 'r')
Lines = file1.readlines()

nb_lines = len(Lines)


nb1 = []  # nb of 1 for each positions
nb0 = []  # nb of 0 for each positions

for i in range(0, len(Lines[0].strip())):
    print("looping len, {}".format(i))
    nb1.append(0)
    nb0.append(0)

for line in Lines:
    line = line.strip()
    for i in range(0, len(line)):
        if line[i:i+1] == "1":
            nb1[i] += 1
        else:
            nb0[i] += 1

gamma = ""
epsil = ""
for i in range(0, len(line)):
    if nb1[i] > nb0[i]:
        gamma += "1"
        epsil += "0"
    else:
        gamma += "0"
        epsil += "1"

# printing the list using loop
for x in range(0, len(nb1)):
    print (nb1[x])
for x in range(0, len(nb0)):
    print (nb0[x])

print("binary Gamma : {} , Epsil : {}".format(gamma, epsil))

gamma = int(gamma, 2)
epsil = int(epsil, 2)
print("final Gamma : {} , Epsil : {}".format(gamma, epsil))

print("quotient : {}".format(gamma * epsil))
