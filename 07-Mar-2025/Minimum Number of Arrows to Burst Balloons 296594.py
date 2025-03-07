# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda point: (point[0] , point[1]))
        count = 0
        curr = points[0][1]
        for i in range(1 , len(points)):
            if curr < points[i][0]:
                count += 1
                curr = points[i][1]
            else:
                curr = min(points[i][1] , curr)
                
        return count + 1
            