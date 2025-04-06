# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ordered = [[] for _ in range(len(nums) + 1)]

        for num , freq in counter.items():
            ordered[freq].append(num)
        ans = []
        for i in range(len(ordered) - 1 , 0 , -1):
            for num in ordered[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans
        

        
            
        
        