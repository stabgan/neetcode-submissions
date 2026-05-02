class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        alphabets = [0]*26
        for i in s :
            alphabets[ord(i)-ord('a')] += 1
        for i in t :
            alphabets[ord(i)-ord('a')] -= 1
        print(alphabets)
        for i in alphabets:
            if i != 0 : return False
        return True

