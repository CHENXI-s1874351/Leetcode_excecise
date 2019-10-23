class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        '''
        count = 0
        
        for i, j in zip(guess, answer):
            
            if i == j:
                count += 1
                
        return count'''

        # One line solution
        return sum([guess[i] == answer[i] for i in range(len(guess))])