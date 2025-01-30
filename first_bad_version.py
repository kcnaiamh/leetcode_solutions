# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         def bsearch(self, l: int, r: int):
#             m = ((r - l) // 2) + l
#             # print(f"l:{l} r:{r} m:{m} | {isBadVersion(m)}")
#             if (r - l + 1) <= 10:
#                 for x in range(l, r + 1):
#                     if isBadVersion(x):
#                         return x
#             elif isBadVersion(m):
#                 r = m + 1
#             else:
#                 l = m
#             return bsearch(self, l, r)
#         return bsearch(self, 1, n)


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = ((r - l) // 2) + l
            # print(f"l:{l} r:{r} m:{m} | {isBadVersion(m)}")
            if (r - l + 1) <= 10:
                for x in range(l, r + 1):
                    if isBadVersion(x):
                        return x
            elif isBadVersion(m):
                r = m + 1
            else:
                l = m