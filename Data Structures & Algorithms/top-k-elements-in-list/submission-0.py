class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        output = []
        for i in nums:
            dic[i] = 1 + dic.get(i, 0)

        array = []
        for value,key in dic.items():
            array.append([key,value])
        
        array.sort()
        for i in range(k):
            n = array.pop()[1]
            output.append(n)
        
        return output
       