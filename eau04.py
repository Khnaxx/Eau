import sys

def fibo(element):
    arr_fibo = [0,1,1,2]
    for i in range(element-len(arr_fibo)+1):
        arr_fibo.append(sum(arr_fibo[-2:]))
    result = arr_fibo[-1]
    return result

if sys.argv[1].isdigit() and len(sys.argv) == 2:
    index = int(sys.argv[1])
    print(fibo(index))
else: print(-1)

