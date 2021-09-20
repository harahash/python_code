from prettytable import PrettyTable


def main():
    print("Cipher of Caesar or Affine system?")
    p = int(input())
    if p == 1:
        print("1. encryption or 2. decryption?")
        p1 = int(input())
        if p1 == 1:
            ceasar_encryption()
        elif p1 == 2:
            ceasar_decryption()
    elif p == 2:
        print("1. encryption or 2. decryption?")
        p1 = int(input())
        if p1 == 1:
            affine_encryption()
        elif p1 == 2:
            affine_decryption()


def ceasar_encryption():
    secret_message = []
    print("Enter your message")
    message = input()
    print("Enter you key")
    key = int(input())
    table = PrettyTable(["Символ сообщ.", "Код символа", "Шифрование", "Код", "Символ шифра"])

    for i in range(0, len(message)):
        x = message[i]
        for j in range(0, 34):
            if alphabet[j] == x:
                symbol = (j+key) % 34
                secret_message.append(alphabet[symbol])
                table.add_row([x, j, (j+key)%34, symbol, alphabet[symbol]])
                continue
    print(table)
    print(secret_message)


def ceasar_decryption():
    message = []
    print("Enter your secret message")
    secret_message = input()
    print("Enter you key")
    key = int(input())
    table = PrettyTable(["Символ шифра", "Код ", "Дешифрование", "Код символа", "Символ сообщ."])

    for i in range(0, len(secret_message)):
        x = secret_message[i]
        for j in range(0, 34):
            if alphabet[j] == x:
                symbol = (j - key) % 34
                message.append(alphabet[symbol])
                table.add_row([x, j, (j - key) % 34, symbol, alphabet[symbol]])
                continue
    print(table)
    print(message)


def affine_encryption():
    secret_message = []
    print("Enter your message")
    message = input()
    print("Enter you key")
    print("0 < k1, k2, < 34")
    key1 = int(input("first key:"))
    key2 = int(input("second key:"))
    key1_1 = key1
    m = 34

    nod = "НОД(" + str(key1_1) + "," + str(m) + ") = "
    while True:
        c = m % key1_1
        print(m, "=", key1_1, "*", m // key1_1, "+", c)
        if c == 0:
            print(nod + str(key1_1))
            break
        m = key1_1
        key1_1 = c

    if key1_1 != 1:
        print("Не выполнено условие НОД(key1, m)=1")
        exit(0)

    table = PrettyTable(["Символ сообщ.", "Код символа", "Шифрование", "Код", "Символ шифра"])

    for i in range(0, len(message)):
        x = message[i]
        for j in range(0, 34):
            if alphabet[j] == x:
                symbol = (key1*j+key2) % 34
                secret_message.append(alphabet[symbol])
                table.add_row([x, j, (key1*j+key2) % 34, symbol, alphabet[symbol]])
                continue
    print(table)
    print(secret_message)


def affine_decryption():
    message = []
    print("Enter your message")
    secret_message = input()
    print("Enter you key")
    print("0 < k1, k2, < 34")
    key1 = int(input("first key:"))
    key2 = int(input("second key:"))
    key1_1 = key1
    m = 34
    m_1 = 34
    a = m
    b = key1
    a_list, b_list = [], []
    u_list, v_list = [], []
    n, v, u = 0, 0, 0

    nod = "НОД(" + str(key1_1) + "," + str(m) + ") = "
    while True:
        c = m % key1_1
        print(m, "=", key1_1, "*", m // key1_1, "+", c)
        if c == 0:
            print(nod + str(key1_1))
            break
        m = key1_1
        key1_1 = c

    if key1_1 != 1:
        print("Не выполнено условие НОД(key1, m)=1")
        exit(0)

    while True:
        n += 1
        a_list.append(a)
        b_list.append(b)
        if b == 0:
            break
        c = a % b
        if c == 0:
            d = b
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

    v = int(v_list[0])
    print("v =", v)

    table = PrettyTable(["Символ шифра.", "Код ", "Дешифрование", "Код символа", "Символ сообщ."])

    for i in range(0, len(secret_message)):
        x = secret_message[i]
        for j in range(0, 34):
            if alphabet[j] == x:
                symbol = ((j + m_1-key2)*v) % 34
                message.append(alphabet[symbol])
                table.add_row([x, j, ((j + m_1-key2)*v) % 34, symbol, alphabet[symbol]])
                continue
    print(table)
    print(message)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', '_', '.', ',', ';',
            ':', "'", '{', '}']

if __name__ == '__main__':
    main()
