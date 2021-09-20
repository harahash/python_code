def main():
    labyrinth = []
    rdl = list(map(int, input().split()))
    n, m = rdl
    for i in range(n):
        rdl = input()
        lvl = []
        for k in range(m):
            if int(rdl[k]) == 1:
                lvl.append(-1)
            else:
                lvl.append(int(rdl[k]))
        labyrinth.append(lvl)
    rdl = list(map(int, input().split()))
    x1, y1 = rdl[0] - 1, rdl[1] - 1
    rdl = list(map(int, input().split()))
    x2, y2 = rdl[0] - 1, rdl[1] - 1
    labyrinth = wave(x1, y1, x2, y2, 1, n, m, labyrinth)
    if labyrinth[x2][y2] > 0:
        print("Can")
    else:
        print("Can not")


def wave(x, y, x2, y2, lvl, n, m, labyrinth):
    labyrinth[x][y] = lvl
    if labyrinth[x][y] == labyrinth[x2][y2]:
        print("Exit found")
        exit()
    if y + 1 < m:
        if labyrinth[x][y + 1] == 0 or (labyrinth[x][y + 1] != -1 and labyrinth[x][y + 1] > lvl):
            print("Right")
            wave(x, y + 1, x2, y2, lvl + 1, n, m, labyrinth)
    if x + 1 < n:
        if labyrinth[x + 1][y] == 0 or (labyrinth[x + 1][y] != -1 and labyrinth[x + 1][y] > lvl):
            print("Bot")
            wave(x + 1, y, x2, y2, lvl + 1, n, m, labyrinth)
    if x - 1 >= 0:
        if labyrinth[x - 1][y] == 0 or (labyrinth[x - 1][y] != -1 and labyrinth[x - 1][y] > lvl):
            print("Top")
            wave(x - 1, y, x2, y2, lvl + 1, n, m, labyrinth)
    if y - 1 >= 0:
        if labyrinth[x][y - 1] == 0 or (labyrinth[x][y - 1] != -1 and labyrinth[x][y - 1] > lvl):
            print("Left")
            wave(x, y - 1, x2, y2, lvl + 1, n, m, labyrinth)
    if y + 1 < m and x - 1 <= 0:
        if labyrinth[x - 1][y + 1] == 0 or (labyrinth[x - 1][y + 1] != -1 and labyrinth[x - 1][y + 1] > lvl):
            print("BotLeft")
            wave(x - 1, y + 1, x2, y2, lvl + 1, n, m, labyrinth)
    if x + 1 < n and y + 1 < m:
        if labyrinth[x + 1][y + 1] == 0 or (labyrinth[x + 1][y + 1] != -1 and labyrinth[x + 1][y + 1] > lvl):
            print("BotRight")
            wave(x + 1, y + 1, x2, y2, lvl + 1, n, m, labyrinth)
    if x - 1 >= 0 and y - 1 >= 0:
        if labyrinth[x - 1][y - 1] == 0 or (labyrinth[x - 1][y - 1] != -1 and labyrinth[x - 1][y - 1] > lvl):
            print("TopLeft")
            wave(x - 1, y, x2, y2, lvl + 1, n, m, labyrinth)
    if y - 1 >= 0 and x + 1 < n:
        if labyrinth[x + 1][y - 1] == 0 or (labyrinth[x + 1][y - 1] != -1 and labyrinth[x + 1][y - 1] > lvl):
            print("TopRight")
            wave(x + 1, y - 1, x2, y2, lvl + 1, n, m, labyrinth)
    return labyrinth


main()
