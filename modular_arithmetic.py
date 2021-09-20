from prettytable import PrettyTable


def main():
    print("Choose the algorithm:")
    print("1. Euclid algorithm (common)")
    print("2. Euclid algorithm (extended)")
    print("3. Algorithm of rapid elevation to degree")
    p = int(input())
    if p == 1:
        euclid_algo()
    elif p == 2:
        euclid_algo_e()
    elif p == 3:
        retd()
    else:
        print("Try again")
        main()


def euclid_algo():
    a = int(input("a = "))
    b = int(input("b = "))
    nod = "НОД(" + str(a) + "," + str(b) + ") = "

    while True:
        c = a % b
        print(a, "=", b, "*", a // b, "+", c)
        if c == 0:
            print(nod + str(b))
            exit(0)
        a = b
        b = c


def euclid_algo_e():
    a = int(input("a = "))
    b = int(input("b = "))
    a_list, b_list = [], []
    u_list, v_list = [], []
    n, v, u = 0, 0, 0
    table = PrettyTable(["Num.", "a", "b", "a % b", "a // b", "d", "u", "v"])

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
            v = (d - a_list[i]*u) // b_list[i]
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
    q = input()


def retd():
    print("x^a(mod n)")
    x = int(input("x = "))
    a = int(input("a = "))
    n = int(input("n = "))
    print("answer with the function pow(x,y[,z]) =", (pow(x, a, n)))
    c = x
    a_bin = bin(a)
    k = len(str(a_bin)[2:])
    b = []
    for i in range(0, k):
        b.append(a_bin[i+2:i+3])
    # print(b)

    for i in range(0, k):
        if i == 0:
            c = (x ** int(b[i])) ** 2 % n
            # print("i = 0")
        else:
            if i == k - 1:
                c = c * x ** int(b[i]) % n
                # print("last")
                print("c =", c)
            if int(b[i]) == 0:
                c = c ** 2 % n
                # print("b[i] = 0")
            elif int(b[i]) == 1:
                c = (c * x) ** 2 % n
                # print("b[i] = 1")


if __name__ == '__main__':
    main()
