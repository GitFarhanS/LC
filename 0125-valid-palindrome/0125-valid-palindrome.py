class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        for char in s:
            if char.isalnum():
                word += char.lower()
        l = 0
        r = len(word) - 1

        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True
