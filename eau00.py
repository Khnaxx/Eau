
def scale(combinaison):
    combinaison = str(combinaison).zfill(3)
    number1, number2, number3 = combinaison[0], combinaison[1], combinaison[2]
    if number1 < number2 < number3:
        return True
    else: return False

arr_diff_number = []
for combinaison in range(12,999):
    if scale(combinaison):
        arr_diff_number.append(combinaison)
for itération in arr_diff_number:
    print(f"{itération:03d}", end = ", ")
