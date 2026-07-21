class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        stone = True
        mA = 0
        
        while l < r:
            mA = max(mA, min(heights[l], heights[r]) * (r-l))

            if heights[l] < heights[r]:
                while heights[l] == heights[l+1] and l < r:
                    l += 1
                l += 1
            elif heights[l] > heights[r]:
                while heights[r] == heights[r-1] and l < r:
                    r -= 1
                r -= 1
            elif heights[l] == heights[r]:
                if heights[l+1] > heights[r-1]:
                    l += 1
                elif heights[l+1] < heights[r-1]:
                    r -= 1
                elif heights[l+1] == heights[r-1]:
                    l += 1
                    r -= 1






        return mA