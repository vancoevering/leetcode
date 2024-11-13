# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return Solution.two_sum_hash_map(nums, target)

    @staticmethod
    def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
        # Brute force solution - O(n*2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # Alternative methods:
    # We could use a binary search, maybe pair the values with their index?
    # Or, we could use a hash-map with {value: index}

    @staticmethod
    def two_sum_hash_map(nums: List[int], target: int) -> List[int]:
        # Let's try the hash-map - O(n?)

        target_is_even = target % 2 == 0
        if target_is_even:
            # In this case, we should check for dupes that are half of target
            half_target = target / 2
            d = dict()
            for i_index, i in enumerate(nums):
                if (i == half_target) and (i in d):
                    return [d[i], i_index]
                d[i] = i_index
        else:
            # In this case, we can ignore dupes
            d = {i: i_index for i_index, i in enumerate(nums)}

        for _ in range(len(d)):
            i, i_index = d.popitem()
            paired_index = d.get(target - i)
            if paired_index is not None:
                return [i_index, paired_index]
