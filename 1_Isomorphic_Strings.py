class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        trackS, trackT = {} , {}

        for i in range(len(s)):
            j, k = s[i], t[i]

            if((j in trackS and trackS[j] != k) or (k in trackT and trackT[k] != j)):
                return False

            trackS[j] = k
            trackT[k] = j
            
        return True
