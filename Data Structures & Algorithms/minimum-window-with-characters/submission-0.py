class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        countS = {} #window

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        current, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")

        left = 0
        for right in range(len(s)):
            countS[s[right]] = countS.get(s[right], 0) + 1
            if s[right] in countT and countS[s[right]] == countT[s[right]]:
                 
                current += 1

            while current == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                countS[s[left]] -= 1
                if s[left] in countT and countS[s[left]] < countT[s[left]]:
                    current -= 1
                left += 1
                
        left, right = res
        return s[left : right+1] if resLen != float("infinity") else ""
        
        


