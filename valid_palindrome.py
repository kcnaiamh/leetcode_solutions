from string import ascii_lowercase, digits

alphanumeric = ascii_lowercase + digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l] not in alphanumeric:
                l += 1
            while r > l and s[r] not in alphanumeric:
                r -= 1

            if s[l] != s[r]:
                return False

            l += 1; r -= 1

        return True