from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram_dict = defaultdict(list)

        for s in strs:
            #first sort the string to check
            sorted_string = tuple(sorted(s)) # this returns a list4, use tuple to make it immutable
            anagram_dict[sorted_string] += [s]
        
        for i in anagram_dict.values():
            result.append(i)
        
        return result
        