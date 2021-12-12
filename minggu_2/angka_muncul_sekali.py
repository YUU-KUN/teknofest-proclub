n = input()
def onlyOne(n):
    output = []
    for i in n:
        if n.count(i) == 1:
            output.append(int(i))
    print(output)

onlyOne(n)