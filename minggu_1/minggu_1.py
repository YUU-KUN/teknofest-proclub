import os
import time

def clean():
    os.system('clear')

def half_Pyramid_pattern(): #DONE
    print('Half Pyramid Pattern')
    for i in range(5):
        for j in range(i+1):
            print("*", end=" ")
        print()

def half_Inverted_pyramid_pattern(): #DONE
    print('Half Inverted Pyramid Pattern')
    for i in range(5):
        for j in range(5-i):
            print("*", end=" ")
        print()

def half_pyramid_pattern_mirrored(): #DONE
    print('Half Pyramid Pattern Mirrored')
    for i in range(5):
        print(((2*5-2)-i*2) * ' ', i*'* ')

def full_pyramid_pattern(): #DONE
    print('Full Pyramid Pattern')
    for i in range(5):
        print((5-i)*' ', i*"* ")

def full_pyramid_pattern_mirrored(): #DONE
    print('Full Pyramid Pattern Mirrored')
    for i in range(5, 0, -1):
        for j in range(5, 0, -1):
            if j <= i:
                print("*", end=" ")
            else:
                print('', end=" ")
        print()

def main ():
    print('''
+-------------------------------------+
| Indra Wahyu | 1301213135 | IF-45-05 |
+-------------------------------------+

[1] Half Pyramid Pattern
[2] Half Inverted Pyramid Pattern
[3] Half Pyramid Pattern Mirrored
[4] Full Pyramid Pattern
[5] Full Pyramid Pattern Mirrored

[0] !!STOP PROGRAM!!
''')

    choose = input("Silahkan Pilih : ")
    if choose == '0':
        print('Program Selesai')
        time.sleep(1)
        clean()
        exit()
    else:
        if choose == "1" or choose.lower() == "half pyramid pattern":
            half_Pyramid_pattern()
            time.sleep(3)
            main()
        elif choose == "2" or choose.lower() == "half Inverted pyramid pattern":
            half_Inverted_pyramid_pattern()
            time.sleep(3)
            main()
        elif choose == "3" or choose.lower() == "half pyramid pattern mirrored":
            half_pyramid_pattern_mirrored()
            time.sleep(3)
            main()
        elif choose == "4" or choose.lower() == "full pyramid pattern":
            full_pyramid_pattern()
            time.sleep(3)
            main()
        elif choose == "5" or choose.lower() == "full pyramid pattern mirrored":
            full_pyramid_pattern_mirrored()
            time.sleep(3)
            main()
        else:
            print('''
            =================
            Input tidak valid
            =================
            ''')
            time.sleep(2)
            main()

main()
