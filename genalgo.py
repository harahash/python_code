from random import *


def initiation():
    g = 0
    s = []
    count = 4
    str_len = 4 #randint(5, 10)
    for i in range(0, count):
        chromosome = []
        for j in range(0, str_len):
            j = randint(0, 1)
            '''
            if j == 2:
                chromosome.append('#')
            else:
            если вернешь #, то поменяй randint(0,2)
            '''
            chromosome.append(j)
        s.append(chromosome)

    print("First population")
    for row in s:
       print("".join(list(map(str, row))))

    crossover(s, count, str_len, g)

'''
def selection(s, str_len, count, g):
    d = []
    for m in range(0, count, 2):
        print(m)
        for i in range(0, str_len):            
            if s[m][i] and s[m+1][i] == '#':
                continue
            if s[m][i] == '#' and s[m+1][i] != '#':
                d.append(m)
                break
            if s[m][i] != '#' and s[m+1][i] == '#':
                d.append(m+1)
                break
            
            if s[m][i] > s[m+1][i]:
                d.append(m+1)
                break
            elif s[m][i] < s[m+1][i]:
                d.append(m)
                break
            else:
                continue
                
    del s[0: count: 2]

    for row in s:
       print("".join(list(map(str, row))))
'''


def crossover(s, count, str_len, g):
    g += 1
    print("Number of generation is", g)
    for m in range(0, count, 2):
        for i in range(0, str_len//2):
            cross = s[m][i]
            s[m][i] = s[m+1][i]
            s[m+1][i] = cross

    #del s[0: count: 10]
    #count //= 10

    #print("after crosselection")
    #for row in s:
    #    print("".join(list(map(str, row))))
    mutation(s, count, str_len, g)

'''
def inversion(s, count, str_len):
    inver_list = []
    for m in range(0, count):
        for i in range(0, str_len//2):
            inver_list.append(s[m][i])
        inver_list.reverse()
        del s[m]
        inver_list.insert(0, inver_list[m])

    print("after inversion")
    for row in s:
        print("".join(list(map(str, row))))
'''


def mutation(s, count, str_len, g):
    m = randint(0, count-1)
    i = randint(0, str_len-1)

    if s[m][i] == 1:
        s[m][i] = 0
    elif s[m][i] == 0:
        s[m][i] = 1

    #print("after mutation")
    #for row in s:
    #    print("".join(list(map(str, row))))

    good_enough(s, count, str_len, g)


def good_enough(s, count, str_len, g):
    for m in range(0, count):
        check = 0
        for i in range(0, str_len):
            if s[m][i] == 1:
                check += 1
    if check == count:
        print("The highest number was received")
        print("The last generation is:")
        for row in s:
            print("".join(list(map(str, row))))
    else:
        crossover(s, count, str_len, g)


initiation()
