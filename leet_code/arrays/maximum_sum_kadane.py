#1480. Running Sum of 1d Array

class MaxSolution:
    def maximum_sum(self,nums) :

        max_ending_here=max_so_far=nums[0]


        for i in range(1, len(nums)):
            max_ending_here=max(A[i],max_ending_here+A[i])
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far
if __name__ == '__main__':
    A=[1, 2, 7, -4, 3, 2, -10, 9, 1]
    print(MaxSolution().maximum_sum(A))
    #print(Solution().rotate(A,3))

'''Problem Statement: Given an integer array arr, find the contiguous 
subarray (containing at least one number) which 
has the largest sum and returns its sum and prints the subarray.

Input: 'arr' = [1, 2, 7, -4, 3, 2, -10, 9, 1]

Output: 11
'''