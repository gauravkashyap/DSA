
class Sort012:
    def sort_num(self,nums) :
        low=0
        mid=0
        high=len(nums)-1
        while mid<high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1

        return nums
if __name__ == '__main__':
    A=[2,0,2,1,1,0]
    print(Sort012().sort_num(A))
    #print(Solution().rotate(A,3))

'''Given an array consisting of only 0s, 1s, and 2s. 
Write a program to in-place sort the array without using 
inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

Input: nums = [0]
Output: [0]

'''