class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key= lambda interval: interval[0])
        matrix=[]
        current= intervals[0]
        for i in range(1, len(intervals)):
            if (current[1]>=intervals[i][0]):
                current[1]= max(current[1], intervals[i][1])
            else:
                matrix.append(current)
                current= intervals[i]
        matrix.append(current)

        return matrix