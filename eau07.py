import sys

if len(sys.argv) == 2 and not sys.argv[1].isdigit():
    string = sys.argv[1]
    string2 = string[0].upper()
    
    for i in range(1,len(string)):
        if string2[-1].isspace():
            string2 += string[i].upper()
        else: string2 += string[i]
    print(string2)

else: print("error.")
