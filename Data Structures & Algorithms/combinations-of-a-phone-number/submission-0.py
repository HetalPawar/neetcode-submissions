class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitstoLetter = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(index, path):
            if len(path) == len(digits):
                res.append(path)
                return

            for i in digitstoLetter[digits[index]]:
                backtrack(index + 1, path + i)
        
        if digits: backtrack(0, "")
        return res