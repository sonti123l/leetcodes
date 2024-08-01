class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string_list = s.rstrip().split(" ")
        last_string = string_list[-1]
        return len(last_string)
