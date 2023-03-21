class Solution:
    def isPalindrome(self, s: str) -> bool:
        #LC 125 - Valid Palindrome
        s1 = "".join(ch for ch in s if ch.isalnum()).lower()
        if s1==s1[::-1]:
            return True
        return False