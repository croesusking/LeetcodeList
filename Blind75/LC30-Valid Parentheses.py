class Solution:
    def isValid(self, s: str) -> bool:
        # LC - Valid Parentheses
        dict1 = {']':'[',')':'(','}':'{'}
        stack =[]
        
        for c in s:
            if c in dict1:
                if not stack:
                    return False
                else:
                    opening = stack.pop()
                    if opening == dict1[c]:
                        continue
                    else:
                        return False
            else:
                stack.append(c)
                
                
        return True if not stack else False
                