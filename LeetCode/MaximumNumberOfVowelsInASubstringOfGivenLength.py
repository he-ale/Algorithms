class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = {"a", "e", "i", "o", "u"}
        for i in range(k):
            if s[i] in vowels:
                count += 1

        maxCount = count

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            if maxCount < count:
                maxCount = count
                if maxCount == k:
                    break
        return maxCount