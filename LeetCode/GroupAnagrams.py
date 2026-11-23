
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dictionary = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = "#".join(map(str, count))

            if key not in dictionary:
                dictionary[key] = []

            dictionary[key].append(word)

        return list(dictionary.values())
            


    