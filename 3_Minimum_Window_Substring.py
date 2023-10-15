class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window, trackT = {}, {}
        curr, goal = 0, 0
        l, r = 0, 0
        ans = ""
        ansLen = float("infinity")

        for i in t:
            trackT[i] = trackT.get(i, 0) + 1
        
        goal = len(trackT)

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in trackT and window[s[r]] == trackT[s[r]]:
                curr+=1

            while curr == goal and l < r:
                if r-l+1 < ansLen:
                    ansLen = r-1+1
                    ans = s[l:r+1]
                if window[s[l]] == trackT.get(s[l], -1):
                    curr-=1
                
                window[s[l]]-=1
                l+=1
        
        return ans
