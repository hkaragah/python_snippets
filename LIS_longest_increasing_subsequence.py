# Objective: find the longest increasing subsequence (LIS) in a given list
# A = [3, 1, 8, 2, 5] => [3, 5] => LIS = 2
# A = [5, 2, 8, 6, 3, 6, 9, 5] => [2, 3, 6, 9] => LIS = 4
# A = [3, 4, -1, 0, 6, 2, 3] => [3, 4, 6] => LIS = 3


# Using dynamic programming
# Using Directed Acyclic Graph (DAG) to find the longest path
# Solving subproblems and storing the results in a table
# LIS[n] = 1 + max{LIS[k] | k < n and A[k] < A[n]}


def sub_lis(A, n, memo={}, prev_index={}):
    if n==0:
        prev_index[n] = -1 # index of the previous element, -1 indicates none  
        memo[n] = 1     
    else:
        prev_index[n] = -1
        prev_lis = [0]
        # Loop over all the previous elements up to A[n], and add their LIS to "prev_lis".
        for i in range(n):
            if A[i] < A[n]:
                try:
                    # If it is computed before
                    prev_lis.append(memo[i]) 
                    if (memo[i] > prev_index[n]): prev_index[n] = i
                except KeyError:
                    # If the LIS is not computed before, use recursive call to compute it.
                    prev_lis.append(sub_lis(A, i))
        memo[n] = 1 + max(prev_lis)
        # prev_index = next((key for key, value in memo.items() if value==max(prev_lis)), -1)
    return lis




def lis(A, memo={}, prev_index={}):  
    for n in range(len(A)):
        sub_lis(A, n, memo, prev_index)
    lis = max(memo.values())
    return lis




def main():
    A = [3, 1, 8, 2, 5]
    # A = [5, 2, 8, 6, 3, 6, 9, 5]
    print(lis(A))
    
        

if __name__=='__main__':
    main()
    