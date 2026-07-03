class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        output = []
        i =0

        while l1 and l2:
            output.append(word1[i])
            output.append(word2[i])
            i+=1
            l1 -=1
            l2 -=1
        if l1:
            output.append(word1[i:])
        elif l2:
            output.append(word2[i:])
        return ''.join(output)