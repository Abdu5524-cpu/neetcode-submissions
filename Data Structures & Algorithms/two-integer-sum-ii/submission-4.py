class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for s in range(0, n):
            for i in range(s+1, len(numbers)):
                if (numbers[s]+numbers[i])==target:
                    return [s+1, i+1]
                    