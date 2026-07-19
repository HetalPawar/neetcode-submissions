class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(index):
            #base case
            if index == len(s):
                res.append(list(path))
                return

            #for loop
            for i in range(index, len(s)):

                #constraints
                if self.ispalindrome(s, index , i):
                    #append, backtrack, remove
                    path.append(s[index: i+1])
                    backtrack(i+1)
                    path.pop()

        backtrack(0)
        return res

    def ispalindrome(self, s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l +=1
            r -=1
        return True