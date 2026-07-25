class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        window=set()
        best=0
        for right in range (len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            window.add(s[right])
            best=max(best,right-left+1)
        return best