import sys

def bool_control(arg):
    for element in arg:
        if element.isalpha():
            print("error.")
            exit()
    else: return True
    
def arr_tri(liste):
    for i in range(len(liste)-1,1,-1):
        for j in range(0,i):
            if liste[j+1] < liste[j]:
                liste[j+1], liste[j] = liste[j], liste[j+1]
    return liste

table = sys.argv[1:]

if bool_control(table):
    table = [int(element) for element in table]
    print(arr_tri(table))
