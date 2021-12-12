def tugas1():
    n = int(input())

    def loop(i, n):
        for k in range(1, n+1):
            print(k*i, end=" ")

    for i in range(1, n+1):
        if 1 <= n <= 30:    
            loop(i,n)
            print()


def merge(list1, list2):
    print(list(set(list1 + list2)))

merge(['kazuya', 'jin', 'lee'], ['kazuya', 'feng'])