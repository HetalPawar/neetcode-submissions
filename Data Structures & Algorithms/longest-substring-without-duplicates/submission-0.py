class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        longest = 0
        sub = []
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l+=1
            
            sub.append(s[r])
            longest = max(longest, r - l + 1)
                
        return longest