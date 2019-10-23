class Solution:
    def removeVowels(self, S: str) -> str:
        '''
        new_s = ''
        for s in S:
            if s not in ['a', 'e', 'i', 'o', 'u']:
                new_s = new_s + s
                
        return new_s'''

        # One line solution
        return "".join([s for s in S if s not in ['a', 'e', 'i', 'o', 'u']])

        # For reminder, if we need to write for-if-else in one line:
        # [f(x) if condition else g(x) for sequence]
        # And if we need to write for-if in one line:
        # [f(x) for sequence if condition]
