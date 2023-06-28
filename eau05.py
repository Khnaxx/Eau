import sys

if len(sys.argv) == 3 and sys.argv[1].isalpha() and sys.argv[2].isalpha() :
    str_global = sys.argv[1]
    str_to_find = sys.argv[2]

    if str_to_find in str_global:
        print("true")
    else:print("false")

else: print("error.")
