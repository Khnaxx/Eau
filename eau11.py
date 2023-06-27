import sys

if not len(sys.argv) < 3 :
    table = sys.argv[1:-1]
    search_element = sys.argv[-1]
    for i in range(len(table)):
        if table[i] == search_element:
            print(i)
            break
    else: print(-1)
        

