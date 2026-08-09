from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<=k:
            return nums
        hashMap={}
        max_elements=[]
        for i in range(len(nums)):
            hashMap[nums[i]]=hashMap.get(nums[i],0)+1
        for i in range(k):
            maximum_frequency=max(hashMap,key=hashMap.get)
            max_elements.append(maximum_frequency)
            del hashMap[maximum_frequency]
        return max_elements
