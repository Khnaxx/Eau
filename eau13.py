import sys

def bool_control(arg):
    for element in arg:
        if element.isalpha():
            print("error.")
            exit()
    else: return True
    
def arr_tri_selection(arr):
    n = len(arr)
    for i in range(0,n-1):
        minimum = i
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                minimum = j
        if minimum != i:
            arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr

table = sys.argv[1:]

if bool_control(table):
    table = [int(element) for element in table]
    print(arr_tri_selection(table))
