class Solution:
    def maxArea(self, height: List[int]) -> int:
        # LC 11 - Container with Most Water
        maxArea = 0
        l=0
        r=len(height)-1
        
        
        while l<r:
            width = r-l
            maxL=height[l]
            maxR=height[r]
            maxArea = max(maxArea,min(maxL,maxR)*width)
            
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
                
        return maxArea