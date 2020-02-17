class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []
        phone = {'2': ['a','b','c'],
                 '3': ['d','e','f'],
                 '4': ['g','h','i'],
                 '5': ['j','k','l'],
                 '6': ['m','n','o'],
                 '7': ['p','q','r','s'],
                 '8': ['t','u','v'],
                 '9': ['w','x','y','z']}
        output = []

        def backtrack(string, nextString):
            if not nextString:
                output.append(string)
            else:
                for ch in phone[nextString[0]]:
                    backtrack(string + ch, nextString[1:])

        backtrack('', digits)
        return output
        
