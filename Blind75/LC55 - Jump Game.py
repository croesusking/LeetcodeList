class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #LC 55 - Jump Game
        goal = len(nums)-1 #goal is the last index
        for i in range(len(nums)-1,-1,-1): #start from end
            if i+nums[i] >= goal: #if i can reach goal
                goal = i #update goal to i
        return True if goal ==0 else False #if goal is 0, then we can reach the end
