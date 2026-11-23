class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        aux= [1] 
        aux2= [1]
        j= len(nums)-1
        for i in range(len(nums)-1):
            aux.append(aux[i]* nums[i])
            aux2.append(aux2[i]* nums[j])
            j-=1
        products= []
        j= len(nums)-1
        for i in range(len(nums)):
            products.append(aux[i]* aux2[j])
            j-=1
        return products


        # products= []
        # frequencies= dict()
        # for num in nums:
        #     frequencies[num]= frequencies.get(num, 0)+ 1
        # keys= frequencies.keys()
        # for num in nums:
        #     aux= 1
        #     for k in keys:
        #         if (k == num):
        #             aux=aux* k**(frequencies[k]-1)
        #         else:
        #             aux=aux* k**(frequencies[k])
        #     products.append(aux)
        # return products
s= Solution()
s.productExceptSelf([1,2,3,4])