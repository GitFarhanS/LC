class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_dict = {}
        count_dict2 = {}
        for char in s:
            count_dict[char] = count_dict.get(char, 0) + 1
        for char in t:
            count_dict2[char] = count_dict2.get(char, 0) + 1


        if count_dict == count_dict2:
            return True
        else:
            return False
