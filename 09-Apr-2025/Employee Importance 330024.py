# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        imp = defaultdict(int)
        sub = defaultdict(list)
        for employee in employees:
            imp[employee.id] = employee.importance
            sub[employee.id] = employee.subordinates
        
        def dfs(node):
            ans = 0
            if not sub[node]:
                return imp[node]
            for nebr in sub[node]:
                    ans += dfs(nebr)
            return ans + imp[node]
        return dfs(id)
        