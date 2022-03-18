# from itertools import combinations
# 
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         result_set = []
#         for comb in combinations(nums, 3):
#             tmp = set(comb)
#            if sum(comb) == 0 and tmp not in result_set:
#                print(tmp, result_set)
#                result.append(comb)
#                 result_set.append(tmp)
#         print('='*10)
#         return result
        
class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            # 첫번째 값이 이전과 같았다면, pass
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum == 0
                    result.append([nums[i],nums[left],nums[right]])
                    
                    # left와 right가 이전 값과 다른 경우로 left, right값 조정
                    while left < right and nums[left]==nums[left+1]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return result