def getRPC(x):
    return {
        'A': 'R',
        'B': 'P',
        'C': 'S',
        'X': 'R',
        'Y': 'P',
        'Z': 'S'
    }[x]


def getScore(x, y):
    return {
        'RR': 3,
        'PP': 3,
        'SS': 3,
        'RP': 0,
        'RS': 6,
        'PR': 6,
        'PS': 0,
        'SR': 0,
        'SP': 6
    }[x+y]


def getChoice(x, y):
    return {
        'RX': 'S',
        'RY': 'R',
        'RZ': 'P',
        'PX': 'R',
        'PY': 'P',
        'PZ': 'S',
        'SX': 'P',
        'SY': 'S',
        'SZ': 'R'
    }[x+y]


def getChoicePoints(x):
    return {
        'R': 1,
        'P': 2,
        'S': 3
    }[x]


file1 = open('2.dat', 'r')
Lines = file1.readlines()

sum = 0
count = 0

sum2 = 0

for i in range(0, len(Lines)):
    a, b = Lines[i].strip().split()
    a = getRPC(a)
    c = getChoice(a, b)
    b = getRPC(b)

    sum += getScore(b, a)
    sum += getChoicePoints(b)
    count += 1

    sum2 += getScore(c, a)
    sum2 += getChoicePoints(c)

print('score : {}'.format(sum))
print('count : {}'.format(count))

print('score 2 : {}'.format(sum2))
