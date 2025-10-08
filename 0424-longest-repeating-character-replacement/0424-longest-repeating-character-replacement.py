class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        right = 0
        largest = 0
        max_freq = 0   # running max frequency

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # shrink the window if replacements exceed k
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            largest = max(largest, right - left + 1)
            right += 1

        return largest
