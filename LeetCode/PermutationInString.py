class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequencies= self.getFrequency(s1)
        slow= 0
        aux= self.getFrequency(s2[0:len(s1)])
        if len(s1)>len(s2):
            return False
        if frequencies == aux:
            return True
        for fast in range(len(s1), len(s2)):
            aux[ord(s2[slow])-ord('a')]-=1
            aux[ord(s2[fast])-ord('a')]+=1
            slow+= 1
            if ( aux == frequencies):
                return True
        return False

    def getFrequency(self, word):
        xs= [0]*26

        for c in word:
            xs[ord(c)-ord('a')]+=1

        return xs