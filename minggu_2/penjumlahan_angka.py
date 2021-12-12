listt = input().split(', ')
target = int(input())

def penumlahan_angka(listt, target):
    output = []
    for i in range(len(listt)):
        for j in range(len(listt)):
            if int(listt[i]) + int(listt[j]) == target:
                output.append(i)
                output.append(j)
        if len(output) == 2:
            break
    print(output)

penumlahan_angka(listt, target)