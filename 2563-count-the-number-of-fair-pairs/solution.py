# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/?envType=daily-question&envId=2024-11-13
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Two-Pointer Attempt 2: Counting pairs less than method
        nums = sorted(nums)
        return Solution.countPairsLessThan(nums, upper + 1) - Solution.countPairsLessThan(nums, lower)

    @staticmethod
    def countPairsLessThan(nums: List[int], ceiling: int) -> int:
        left = 0
        right = len(nums) - 1
        result = 0

        while left < right:
            sum = nums[left] + nums[right]
            if sum < ceiling:
                result += right - left
                left += 1
            else:
                right -= 1

        return result
