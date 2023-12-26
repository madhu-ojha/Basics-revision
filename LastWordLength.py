# Leetcode 58
# Length of Last word

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        wordToList = []
        s = s.split()
        lastword = s[-1]
        return len(lastword)


# string1 = "Hello! Its me Madhu Sudan Ojha."
string1 = input("Enter a string: ")
word = Solution()
print(word.lengthOfLastWord(string1))
