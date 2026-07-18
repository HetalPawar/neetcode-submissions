class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        prefix = ''

        for i in range(len(strs[0])):
            candidate = prefix + strs[0][i]

            for word in strs:
                if not word.startswith(candidate):
                    return prefix
                
            prefix = candidate

        return prefix