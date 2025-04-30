# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapify(heap)
        ans = 0
        for i in range(1 , len(heights)):        
            if heights[i] > heights[i - 1]:
                heappush(heap , heights[i] - heights[i - 1])
                if len(heap) == ladders + 1:
                    if bricks >= heap[0]:
                        bricks -= heappop(heap)
                    else:
                        return i - 1
              
        return len(heights) - 1
        