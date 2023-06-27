import sys

    
def arr_sort_ASCII(arr):
    for i in range(len(arr)-1,1,-1):
        for j in range(0,i):
            if ord(arr[j+1][0]) < ord(arr[j][0]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

def bool_control(arg):
    for element in arg:
        if element.isdigit():
            print("error.")
            exit()
    else: return True
    
if len(sys.argv) == 1:
    print("error.")
    exit()
table = sys.argv[1:]
if bool_control(table):
    table = [element for element in table]
    print(arr_sort_ASCII(table))

