from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we create an empty hashmap
        # we will add element of list as key and index as value as we iterate through the loop
        hashMap={}
        for i in range(len(nums)):
            complement=target-nums[i]
            # check whether the complement was added previously in the hashmap
            if complement in hashMap:
                return [i,hashMap[complement]]
            # if not added add the particular element of the list to the hashmap
            hashMap[nums[i]]=i
        return[]
