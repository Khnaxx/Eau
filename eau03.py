import sys

if len(sys.argv) == 1:
    print("erreur.")
else:
    arr_input = sys.argv[1:]

    for arg in reversed(arr_input):
        print(arg)
