class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = {}
        for x in s:
            if x not in hmap:
                hmap[x] = 1
            else:
                hmap[x] += 1

        cnt, has_odd = 0, 0
        for x in hmap.values():
            if x & 1 == 1:
                has_odd = 1
                cnt += x - 1
                continue
            cnt += x
        # print(hmap)
        return cnt + has_odd

print(Solution().longestPalindrome("abccccdd"))