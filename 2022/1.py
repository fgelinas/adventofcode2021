file1 = open('1.dat', 'r')
Lines = file1.readlines()

Lines.append('')

sum = 0
max = 0
max2 = 0
max3 = 0
for i in range(1, len(Lines)):
    l = Lines[i].strip()
    if (l == ''):
        if sum > max:
            max3 = max2
            max2 = max
            max = sum
        sum = 0
    else:
        sum += int(l)


print('max found : {}'.format(max))
sum = max + max2 + max3
print('sum top 3 found : {}'.format(sum))
