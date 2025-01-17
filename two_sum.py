# import bisect

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         idx_num = [(x, i) for i, x in enumerate(nums)]
#         idx_num.sort(key=lambda x: x[0])

#         for i, num in enumerate(nums):
#             target_pos = bisect.bisect_left(idx_num, (target - num, -1))
#             # print(f"OUT: num: {num}, comp: {target - num}")
#             if target_pos < len(nums) and idx_num[target_pos][1] != i and idx_num[target_pos][0] + num == target:
#                 # print(f"IN: num: {num}, target_pos: {target_pos}, comp: {idx_num[target_pos][0]}")
#                 return [i, idx_num[target_pos][1]]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_bucket = {}
        for i, x in enumerate(nums):
            if (target - x) in prev_bucket:
                return [i, prev_bucket[target - x]]
            prev_bucket[x] = i



lst = [2,7,11,15]
target = 9
print(Solution().twoSum(lst, target))