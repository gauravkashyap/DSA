class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        X={}
        res=[]
        for i in range(len(nums)):
            if (target - nums[i]) in X:
                res.append(X[target-nums[i]])            
                X[nums[i]]=i
                res.append(i)
                break
            else:
                X[nums[i]]=i
        return res
        
        
            