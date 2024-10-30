"""

DYNAMIC PROGRAMMING:

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
and you want to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?


"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        """
        
        1. compare t[0] w/ s characters
        2. if find a match at s[i]:
            a. drop t[0] from t
            b. drop s[:i] from s
           else:
            return False 
        3. repeat 1-2 until there is no more char in t
        4. return True
        """
        i = 0
        j = 0
        flag = False
        while i < len(s):
            
            while j < len(t):
                if s[i] == t[j]:
                    j += 1
                    flag = True
                    break
                else:
                    j += 1
            
            if flag: # change the status of the flag for the next s-character
                flag = False
            else: # means that s[i] does not exit in t. Stop
                return False
            
            i += 1
            
        return True  
    
    
    
def main():
    s = "abc"
    t = "ahbgdc"   
    print(Solution().isSubsequence(s, t))
    
    s = "axc"
    t = "ahbgdc"   
    print(Solution().isSubsequence(s, t))
    
    s = "b"
    t = "abc"   
    print(Solution().isSubsequence(s, t))
    
import os
if __name__ == "__main__":
    os.system('cls')
    main()