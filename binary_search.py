from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect_left(nums, target)
        return -1 if nums[i] != target else i