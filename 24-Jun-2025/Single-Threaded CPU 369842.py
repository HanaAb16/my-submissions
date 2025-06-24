# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        tasks.sort()
        cur_time = tasks[0][0]
        ans = []
        hp = []
        i = 0
        while i < n:
            while i < n and cur_time >= tasks[i][0]:
                heappush(hp , (tasks[i][1] , tasks[i][2]))
                i += 1
            if hp:
                pr_time , ind = heappop(hp)
                ans.append(ind)
                cur_time += pr_time
            else:
                cur_time = tasks[i][0]
        while hp:
           ans.append(heappop(hp)[1])         
        return ans

