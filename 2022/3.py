import string


def getPriority(a):
    ref = string.ascii_lowercase + string.ascii_uppercase
    return ref.find(a) + 1


file1 = open('3.dat', 'r')
Lines = file1.readlines()

sum1 = 0
sum2 = 0

group = []

for i in range(0, len(Lines)):
    l = Lines[i].strip()
    a = l[:len(l)//2]
    b = l[len(l)//2:]

    print(a + " " + b)

    for z in range(0, len(a)):
        if (b.find(a[z]) >= 0):
            print("found : " + a[z])
            sum1 += getPriority(a[z])
            break

    # part 2
    group.append(l)
    if (len(group) == 3):
        print("got a group of 3 : " +
              group[0] + " " + group[1] + " " + group[2])

        for z in range(0, len(group[0])):
            if (group[1].find(group[0][z]) >= 0 and group[2].find(group[0][z]) >= 0):
                print("Found group item : " + group[0][z])
                sum2 += getPriority(group[0][z])
                break
        group = []

print("Sum : " + str(sum1))
print("Sum2 : " + str(sum2))
