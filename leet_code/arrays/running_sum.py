#1480. Running Sum of 1d Array

class Solution:
    def runningSum(self,nums) :
        res = []
        s = 0
        for i in range(0, len(nums)):
            s = s + nums[i]
            res.append(s)
        return res
if __name__ == '__main__':
    A=[ 1, 2, 3, 4 ]
    print(Solution().runningSum(A))
    #print(Solution().rotate(A,3))

'''Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''