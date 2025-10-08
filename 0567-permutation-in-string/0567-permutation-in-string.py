class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        # Build frequency dictionary for s1
        word = {}
        for char in s1:
            word[char] = word.get(char, 0) + 1

        # Build initial window for s2
        window = {}
        for i in range(len1):
            window[s2[i]] = window.get(s2[i], 0) + 1

        if window == word:
            return True

        # Slide the window
        for i in range(len1, len2):
            # Add new char
            window[s2[i]] = window.get(s2[i], 0) + 1
            # Remove old char
            old_char = s2[i - len1]
            window[old_char] -= 1
            if window[old_char] == 0:
                del window[old_char]

            if window == word:
                return True

        return False
