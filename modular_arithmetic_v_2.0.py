import math
from prettytable import PrettyTable


def main():
    print("Choose the algorithm you want to use:")
    print("1. Calculation of inverse quantities")
    print("2. The first-degree comparisons")
    p = int(input())
    if p == 1:
        print("Choose the way")
        print("1. With table")
        print("2. With Euler's function")
        print("3. with advanced Euclidean algorithm")
        p1 = int(input())
        if p1 == 1:
            inverse_quantities_w_table()
        if p1 == 2:
            inverse_quantities_w_euler_func()
        if p1 == 3:
            inverse_quantities_w_euclidean_algo()
    elif p == 2:
        first_degree_comparisons()
    else:
        print("You put wrong number. Try again.")
        main()


def inverse_quantities_w_table():
    print("Calculation of inverse quantities with table")
    print("a*x=1(mod n)")
    print("x = a^(-1)(mod n)")
    a = int(input("a = "))
    n = int(input("n = "))
    a1 = a
    n1 = n
    print(str(a)+"*x=1(mod "+str(n)+")")
    nod = "НОД(" + str(n) + "," + str(a) + ") = "
    while True:
        c = n % a
        print(n, "=", a, "*", n // a, "+", c)
        if c == 0:
            print(nod + str(a))
            break
        n = a
        a = c

    table = PrettyTable(["x", str(a1)+"*x", str(a1)+"*x(mod"+str(n1)+")"])
    i_list = []
    ai_list = []
    aimodn_list = []
    for i in range(1, n1):
        i_list.append(i)
        ai_list.append(a1*i)
        aimodn_list.append(a1*i % n1)
        if a1*i % n1 == 1:
            result = i

    for j in range(0, n1-1):
        table.add_row([i_list[j], ai_list[j], aimodn_list[j]])
    print(table)
    print("Result:", "x = " + str(a1)+"^-1(mod"+str(n1)+")="+str(result))


def inverse_quantities_w_euler_func():
    print("Calculation of inverse quantities with Euler's function")
    print("a*x=1(mod n)")
    print("x = a^(-1)(mod n)")
    a = int(input("a = "))
    n = int(input("n = "))
    print(str(a) + "*x=1(mod " + str(n) + ")")

    if (math.factorial(n-1)+1) % n != 0:  # Wilson's theorem
        print("non-simple number")
    else:
        print(n, "is simple number")
        f = n - 1
    print(str(a)+"^("+str(f)+"-1)(mod"+str(n)+")")

    f_bin = bin(f-1)
    k = len(str(f_bin)[2:])
    b = []
    for i in range(0, k):
        b.append(f_bin[i+2:i+3])

    for i in range(0, k):
        if i == 0:
            c = (a ** int(b[i])) ** 2 % n
            # print("i = 0")
        else:
            if i == k - 1:
                c = c * a ** int(b[i]) % n
                print("Result is", c)
                break
            if int(b[i]) == 0:
                c = c ** 2 % n
            elif int(b[i]) == 1:
                c = (c * a) ** 2 % n

    print("Check")
    print(str(a)+"*"+str(c)+"=1(mod"+str(n)+")")
    if a*c % n == 1:
        print("The result is correct")
    else:
        print("the result isn't correct")


def inverse_quantities_w_euclidean_algo():
    a = int(input("n = "))
    b = int(input("a = "))
    b1 = b
    a_list, b_list = [], []
    u_list, v_list = [], []
    n, v, u = 0, 0, 0
    table = PrettyTable(["Num.", "n", "a", "n % a", "n//a", "d", "u", "v"])

    nod = "НОД(" + str(a) + "," + str(b) + ") = "
    while True:
        n += 1
        a_list.append(a)
        b_list.append(b)
        if b == 0:
            break
        c = a % b
        if c == 0:
            d = b
            print(nod + str(d))
        a = b
        b = c

    a_list.reverse()
    b_list.reverse()

    for i in range(0, n):
        if i == 0:
            u = (d - b_list[0] * v) // a_list[0]
            u_list.append(u)
            v_list.append(v)
        else:
            u = v
            v = (d - a_list[i] * u) // b_list[i]
            u_list.append(u)
            v_list.append(v)

    a_list.reverse(), b_list.reverse()
    u_list.reverse(), v_list.reverse()

    for i in range(0, n):
        if b_list[i] == 0:
            mod = "-"
            div = "-"
        else:
            mod = a_list[i] % b_list[i]
            div = a_list[i] // b_list[i]
        table.add_row([i + 1, a_list[i], b_list[i], mod, div,
                       d, u_list[i], v_list[i]])

    print(table)

    if d > 1 and b1 % d != 0:
        print("The equation has no solutions")
    elif d == 1:
        print("The equation has one solution")
    elif d > 1 and b1 % d == 0:
        print("The equation has "+str(d)+" solutions")


def first_degree_comparisons():
    pass


if __name__ == '__main__':
    main()
