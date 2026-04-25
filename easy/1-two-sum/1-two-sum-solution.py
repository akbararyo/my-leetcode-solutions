class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print(range(len(nums)))
        # print(range(1,len(nums)))
        answer=[]
        for i in range(len(nums)):
            # print(f"{i}i")
            for j in range(i+1,len(nums)):
                # print(f"{j}j")
                if nums[i]+nums[j]==target:
                    # print(nums[i]+nums[j])
                    # print(f"{i}i and {j}j")
                    # answer.append(i)
                    # answer.append(j)
                    answer.extend([i,j])
                    return(answer)
        
