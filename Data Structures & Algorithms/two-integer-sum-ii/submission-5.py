class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)-1
        l = 0
        duo = None
        while not duo:
            if nums[l] + nums[n] == target:
                return [l+1, n+1]
            elif nums[l] + nums[n] > target:
                n -= 1
            else:
                l += 1

