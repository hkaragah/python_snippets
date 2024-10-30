"""
GRAPH:

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        # If there is only one person and no trust, they are the judge by default
        if n == 1 and not trust:
            return 1
        
        # Initialize in-dgree and out-dgree lists
        in_degree = [0] * (n + 1) 
        out_dgree = [0] * (n + 1)
        
        # If a person trust someone, their out-degree increases
        # If a person is trusted by someone else, their in-degree increases
        for a, b in trust:
            out_dgree[a] += 1
            in_degree[b] += 1
            
        # Find town judge who:
        # Has an out-dgree of 0 (trusts no one)
        # Has an in-dgree of n-1 (is trusted by everyone else)
        for person in range(1, n + 1):
            if out_dgree[person] == 0 and in_degree[person] == n - 1:
                return person
        return -1
        
        
def main():
    trust1 = [[1,2]]
    trust2 = [[1,3],[2,3]]
    trust3 = [[1,3],[2,3],[3,1]]
    trust4 = [[1,2],[2,3]]
    
    s = Solution()
    print(s.findJudge(2, trust1)) # output: 2
    print(s.findJudge(3, trust2)) # output: 3
    print(s.findJudge(3, trust3)) # output: -1
    print(s.findJudge(3, trust4)) # output: -1
    
    
import os
if __name__ == "__main__":
    os.system('cls')
    main()