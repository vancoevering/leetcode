class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_bound = 0
        upper_bound = len(nums) - 1

        while(lower_bound <= upper_bound):
            index = (upper_bound + lower_bound) // 2
            value = nums[index]
            
            if value == target:
                return index
            
            if value < target:
                lower_bound = index + 1
                continue
            
            if value > target:
                upper_bound = index - 1
                continue
        
        return -1
