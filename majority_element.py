# from typing import List

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         freq = {}
#         for x in nums:
#             if x not in freq:
#                 freq[x] = 1
#             else:
#                 freq[x] += 1
#         mx, mx_num = 0, 0
#         for x in freq.keys:
#             if freq[x] > mx:
#                 mx_num = x
#                 mx = freq[x]
#         return mx_num


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = majority = 0
        for x in nums:
            if majority == 0:
                res = x
            majority += (1 if res == x else -1)
        return res