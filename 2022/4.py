file1 = open('4.dat', 'r')
Lines = file1.readlines()

sum = 0
sum2 = 0
for i in range(0, len(Lines)):
    l = Lines[i].strip()

    a, b = l.split(",")

    a1, a2 = a.split("-")
    a1 = int(a1)
    a2 = int(a2)
    b1, b2 = b.split("-")
    b1 = int(b1)
    b2 = int(b2)
    if (b1 >= a1 and b2 <= a2) or (a1 >= b1 and a2 <= b2):
        sum += 1

    if (b1 >= a1 and b1 <= a2) or (b2 >= a1 and b2 <= a2) or (a1 >= b1 and a1 <= b2) or (a2 >= b1 and a2 <= b2):
        print("overlap : " + l)
        sum2 += 1
    else:
        print("not overlap : " + l)

print("sum found : " + str(sum))
print("sum 2 : " + str(sum2))
