class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        memo = []
        i = 0
        print(nums)
         

        while i <= n-3:
            l = i+1
            r = n-1
            
            while l < r:
                diff = nums[i] + nums[l] + nums[r]
                if diff == 0:
                    memo.append([nums[i], nums[l], nums[r]])
                    while nums[r] == nums[r-1]  and l < r-1:
                        r -= 1
                    while nums[l] == nums[l+1]  and l < r-1:
                        l += 1
                    r -= 1
                    l += 1
                elif diff > 0:
                    while nums[r] == nums[r-1] and l < r-1:
                        r -= 1
                    r -= 1
                else:
                    while nums[l] == nums[l+1] and l < r-1:
                        l += 1
                    l += 1
            
            print(i)

           

            while nums[i] == nums[i+1] and i < n-2:
                i += 1

            i += 1

        return memo
        