n = input().split(', ')
kemunculan = []

def total_kemunculan(n):
    dict = {}
    for i in set(n):
        print('{}: {}'.format(i.replace('\"', ''), n.count(i)))
        dict[i.replace('\"', '')] = n.count(i)
    # print(dict)

total_kemunculan(n)