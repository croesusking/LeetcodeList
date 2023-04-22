class Solution:
    def minInsertions(self, s: str) -> int:
        #LC1312 - Minimum Insertion Steps to Make a String Palindrome
        memo = [[-1]*501 for _ in range(501)]

        def dp1(left, right):
            if left > right:
                return 0
            if memo[left][right] != -1:
                return memo[left][right]
            
            if s[left] == s[right]:
                memo[left][right] = dp1(left+1, right-1)
                return memo[left][right]
            
            memo[left][right] = min(dp1(left, right-1), dp1(left+1, right)) + 1
            return memo[left][right]
        
        
        return dp1(0,len(s)-1)