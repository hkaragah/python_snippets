from time import time



def fib_recursive(n):
    if n<=1:
        return n
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)



def fib_dynamic(n, memo = {}):
    try:
        return memo[n]
    except KeyError:
        if n<= 1:
            result = n
        else:
            result = fib_dynamic(n-1) + fib_dynamic(n-2)
        memo[n] = result
        return result



def fib_buttom_up(n):
    if n <= 1:
        return n
    buttom_up = [0] * (n+1)
    buttom_up[1] = 1
    buttom_up[2] = 1
    for i in range(3, n+1):
        buttom_up[i] = buttom_up[i-1] + buttom_up[i-2]
    return buttom_up[n]



def time_it(func, n):
    start = time()
    result = func(n)
    end = time()
    print(f"{func.__name__}({n}): {result}")
    print(f"Time elapsed: {end - start}\n")
    
    
  
def main():

    n = 500
    
    # Measure the recursive method runtime
    # time_it(fib_recursive, n)

    # Measure the dynamic method runtime
    time_it(fib_dynamic, n)
    
    # Measure the buttom-up method runtime
    time_it(fib_buttom_up, n)
    
if __name__=='__main__':
    main()
    