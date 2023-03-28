class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # LC 76 - Minimum Window Substring
        if t =="":return ""
        
        countT = Counter(t)
        window={}
        
        have,need = 0, len(countT)
        
        res = [-1,-1]
        resLen = float('inf')
        
        l=0
        for r in range(len(s)):
            char = s[r]
            
            window[char] = 1 + window.get(char,0)
            
            if char in countT and window[char]==countT[char]:
                have+=1
                
                
            while have == need:
                if (r-l+1)<resLen:
                    resLen = (r-l+1)
                    res = [l,r]
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen!=float('inf') else ""