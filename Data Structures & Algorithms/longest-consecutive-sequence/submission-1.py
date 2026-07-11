class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        setnums = set(nums) #to skip duplicate nums
        longest = 0

        for i in setnums:
            if (i-1) not in setnums: #it is the smallest number for its sequence
                curr = 1 #initializign the curr lenght as 1
                while (i+curr) in setnums: #till the next number in seq exists, keep increasing curr
                    curr += 1
            else:
                curr = 1
            longest = max(longest, curr) #the calculated lenght or previous
        return longest