lass Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        checkSet = set()

        while r < len(s):
            while s[r] in checkSet:
                checkSet.remove(s[l])
                l += 1

            checkSet.add(s[r])
            maxLen = max(maxLen, r-l+1)
            r += 1
        
        return maxLen
