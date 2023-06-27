import sys

if len(sys.argv) == 3 and sys.argv[1].isdigit():
    
    first_value = int(sys.argv[1])
    second_value = int(sys.argv[2])
    if first_value < second_value:
        for i in range(first_value, second_value):
            print(i, end = " ")
    else:
        for i in range(second_value, first_value):
            print(i, end = " ")
        
else : print("error.")
    
