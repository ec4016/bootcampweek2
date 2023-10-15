class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) < 1:
            return ""

        window, trackT = {}, {}
        curr, goal = 0, 0

        for i in t:
            trackT[i] = trackT.get(i, 0) + 1
        
        goal = len(trackT)

        for j in range(len(s)):
            window(s[r]) = window.get(s[r], 0) + 1

            if s[r] in trackT and window[s[r]] == trackT[c]:
                curr += 1

            while curr == goal:
                # stuck
