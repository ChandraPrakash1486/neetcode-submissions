class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        res = 0

        while i < j:
            width = j - i
            height = min(heights[i], heights[j])
            area_of_water = width * height
            res = max(res, area_of_water)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return res


        
        