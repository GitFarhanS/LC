class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}  # closing -> opening

        for br in s:
            if br in mapping:  # If it's a closing bracket
                if not stack or stack[-1] != mapping[br]:
                    return False
                stack.pop()
            else:  # Opening bracket
                stack.append(br)

        return not stack