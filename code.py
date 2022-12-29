class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        maxprod,minprod=ans,ans
		
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxprod,minprod=minprod,maxprod
                
            maxprod=max(nums[i],maxprod*nums[i])
            minprod=min(nums[i],minprod*nums[i])
            ans=max(ans,maxprod)
            
        return ans

        '''
Traverse L-R and keep storing the min product and max product.
If current val is 0 or neg, swap the min and max product bcz Max value when mulitplied to neg, 
will be the minimum value now ( 100 * -2 = -200 ) and vice versa.
'''
