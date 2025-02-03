class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_character_count = [0] * 26
        m_character_count = [0] * 26
        for x in ransomNote:
            rn_character_count[ord(x) - 97] += 1
        for x in magazine:
            m_character_count[ord(x) - 97] += 1

        for x in range(26):
            if rn_character_count[x] > m_character_count[x]:
                return False
        return True