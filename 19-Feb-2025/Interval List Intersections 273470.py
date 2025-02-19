# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(firstList)):
            for j in range(len(secondList)):
                start = max(firstList[i][0] , secondList[j][0])
                end = min(firstList[i][1] , secondList[j][1])
                if start <= end:
                    ans.append([start , end])
                else:
                    continue
        return ans