class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        aux= nums1[0: m]
        i= 0
        j= 0
        index= 0
        while (i<m and j<n): 
            if(aux[i]<nums2[j]):
                nums1[index]= aux[i]
                i+=1
            else:
                nums1[index]= nums2[j]
                j+=1
            index+=1
        while (i<m):
            nums1[index]= aux[i]
            i+=1
            index+=1
        while (j<n):
            nums1[index]= nums2[j]
            j+=1
            index+=1
            