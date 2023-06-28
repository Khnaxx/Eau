import sys

# vérifie si l'argument est bon

# boucle qui ajoute 1 à l'argument tant qu'il n'est pas premier

def int_find_next_first_number(number):
    while True:
        if not (number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0):
            result = number
            break
        number += 1
                
    return result

if sys.argv[1].isdigit() and len(sys.argv) == 2:
    print(int_find_next_first_number(int(sys.argv[1])))
else: print(-1)
