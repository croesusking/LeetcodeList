class Solution:
    def removeStars(self, s: str) -> str:
        #LC 2390 - Remove Stars From a String
        stack1 = []
        
        
        for c in s:
            if c!="*":
                stack1.append(c)
            else:
                stack1.pop()
                
                
        return "".join(stack1)