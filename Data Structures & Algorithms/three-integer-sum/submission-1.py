class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        temp = [(y,x) for x,y in enumerate(nums)]
        refer = dict()
        for x,y in enumerate(nums):
            if y in refer:
                refer[y].append(x)
            else:
                refer[y] = [x]

        n = len(nums)
        
        memo = set()


        loops = 0
        for i in range(n):
            

            for idx in range(i+1, n):
                loops += 1
                elt = nums[idx]

                diff = -(nums[i] + elt)

                if diff in refer:

                    if max(refer[diff]) > idx:
                        tupl = tuple((nums[i], elt, diff))
                        memo.add(tupl)

        return list(memo)
