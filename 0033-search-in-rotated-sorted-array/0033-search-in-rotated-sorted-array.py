class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        def b_search(l,r):
            while l <= r:
                print(l,r)
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
    
        while l <= r:
            mid = (l +r) //2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid +1

        result = b_search(0,mid-1)
        if result != -1:
            return result
        
        return b_search(mid, len(nums)-1)