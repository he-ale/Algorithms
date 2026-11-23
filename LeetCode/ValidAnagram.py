class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS= dict()
        dictT= dict()
        if (len(s)!=len(t)):
            return False

        for i in range(len(s)):
            if s[i] not in dictS:
                dictS[s[i]] = 1
            else:
                dictS[s[i]]+= 1 
            
            if t[i] not in dictT:
                dictT[t[i]] = 1
            else:
                dictT[t[i]]+= 1

        return dictT == dictS 