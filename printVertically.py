class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        outputs = []
        i = 0
        while True:
            output = ''
            for string in s:
                if i < len(string):
                    output += string[i]
                else:
                    output += ' '
            output = output.rstrip()
            i += 1
            if output == '': break
            outputs.append(output)
        return outputs