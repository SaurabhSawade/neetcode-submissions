class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        max_count = 1
        if not nums:
            return 0
        for i in range(len(nums)-1):
            
            if nums[i]+1 == nums[i+1]:
                count += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                count = 1
            max_count = max(count,max_count)
        return max_count    

