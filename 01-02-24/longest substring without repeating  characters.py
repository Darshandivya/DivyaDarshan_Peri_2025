# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# #Explanation: The answer i
# s consists of English letters, digits, symbols and spaces.



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m=0
        for i in range(len(s)):
            l=[]
            c=0
            for j in range(i,len(s)):
                if s[j] not in l:
                    l.append(s[j])
                    c+=1
                    m=max(m,c)
                else:
                    break
        return m
