class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        #LC 15 - 3Sum
        
        for i,c in enumerate(nums):
            if i>0 and nums[i-1]==c:
                continue
                
            l=i+1
            r=len(nums)-1
            
            while l<r:
                threeSum = nums[l]+c+nums[r]
                
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([nums[l],c,nums[r]])
                    l+=1
                    
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                        
        return res