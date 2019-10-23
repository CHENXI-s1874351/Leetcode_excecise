class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        position = 0
        count = 0
        
        for s in word:
            
            index = keyboard.index(s)
            count += abs(index - position)
            position = index
        
        return count

        # We can also apply hash table to this problem.
        # First we create a dict object to store each character 
        # and their corresponding postions in the keyboard.
        # Then we use ideas above to solve the problem.
        # Note that time complexity of the hash table version solution is O(m+n),
        # while time complexity of solution above is O(mn), where n refers to
        # the length of keyboard and m refers to the length of word.