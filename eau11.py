import sys

def bool_control(arg):
    for element in arg:
        if element.isalpha():
            print("error.")
            exit()
    else: return True

def int_min_abs(table):
    min_abs = abs(sum(table))
    for i in table:
        for j in table:
            difference = abs(abs(i) - abs(j))
            if difference < min_abs and difference != 0:
                min_abs = difference
    return min_abs
            

table = sys.argv[1:]

if bool_control(table):
    table = [int(element) for element in table]
    print(int_min_abs(table))
    
