def timesTables():
    for i in range(1, 13, 2):
        print(*range(i, i * 13, i + i))

timesTables()
