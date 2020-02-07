class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_list = str.split()
        if len(pattern) != len(str_list): return False
        pattern_to_string = {}
        string_to_pattern = {}
        for ch, string in zip(pattern, str_list):
            if ch not in pattern_to_string:
                pattern_to_string[ch] = string
            else:
                if pattern_to_string[ch] != string:
                    return False
            if string not in string_to_pattern:
                string_to_pattern[string] = ch
            else:
                if string_to_pattern[string] != ch:
                    return False           
        return True
