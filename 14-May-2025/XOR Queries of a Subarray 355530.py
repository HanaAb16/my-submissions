# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr_xor = [0]
        for num in arr:
            arr_xor.append(arr_xor[-1] ^ num)
        ans = []
        for l , r in queries:
            ans.append(arr_xor[l] ^ arr_xor[r + 1])
        return ans
        