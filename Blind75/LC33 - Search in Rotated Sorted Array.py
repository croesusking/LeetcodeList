class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # LC 33 - Search in Rotated Sorted Array
        l=0
        r = len(nums)-1

        while l<=r:
            mid = l + (r-l)//2

            if nums[mid]==target:
                return mid
            elif nums[mid] >=nums[l]:
                if target>=nums[l] and target < nums[mid]:
                    r = mid-1  #search left
                else:
                    l = mid+1 #search right
            else:
                if target<=nums[r] and target>nums[mid]:
                    l=mid+1 #search right
                else:
                    r=mid-1 #search left


        return -1
