# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u , v in prerequisites:
            graph[v].append(u)
        res = defaultdict(set)
        visited = [0] * numCourses
        def dfs(node):
            pre = set()
            for neb in graph[node]:
                if not visited[neb]:
                    visited[neb] = 1
                    pre.update(dfs(neb))
                else:
                    pre.update(res[neb])
                    pre.add(neb)
            res[node].update(pre)
            pre.add(node)
            return pre
        for i in range(numCourses):
            if not visited[i]:
                visited[i] = 1
                dfs(i)
        ans = []
        for u , v in queries:
            if u in res[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
