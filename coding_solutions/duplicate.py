class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m=len(nums)
        i=0
        j=1
        while(j<m):
            if nums[i]==nums[j]:
                nums.remove(nums[j])
                m-=1
            else:
                i=j
                j+=1
            