class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def generate_ab(n, current="", open_count=0, close_count=0):
            if len(current) == 2 * n:
                output.append(current)
                return

            if open_count < n:
                generate_ab(n, current + "(", open_count + 1, close_count)

            if close_count < open_count:
                generate_ab(n, current + ")", open_count, close_count + 1)
        generate_ab(n)
        return output
        
