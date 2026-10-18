class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in  numSet:
            if num - 1 not in numSet:
                current_num = num
                current_length = 1

                while current_num+1 in numSet:
                    current_num += 1
                    current_length += 1
                res = max(res, current_length)

        return res
