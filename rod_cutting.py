from math import inf
import os
import time

# price table
p = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

def recursive_cut_rod(p, n):
    solution = []
    if n == 0:
        return 0
    q = -inf
    for i in range(1, n+1):
        q = max(q, p[i] + recursive_cut_rod(p, n - i))
    return q
        
def time_solution(cut_func, n):
    start = time.perf_counter()
    r = cut_func(p, n)
    end = time.perf_counter()
    print(f'r: {r} - time elasped: {(end - start):.6f}')
    
def main():
    os.system('cls')
    # for i in range(1, 11):
    #     print(f'r{i} = {recursive_cut_rod(p, i)}')
    time_solution(recursive_cut_rod, 10)
        

if __name__ == '__main__':
    main()