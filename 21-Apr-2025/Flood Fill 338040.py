# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1 , 0) , (0 , 1) , (-1 , 0) , (0 , -1)]
        in_bound = lambda a , b: 0 <= a < len(image) and 0 <= b < len(image[0])
        or_color = image[sr][sc]
        if or_color != color:
            queue = deque([(sr , sc)])
            image[sr][sc] = color
            while queue:
                r , c = queue.popleft()
                for d in directions:
                    newr = r + d[0]
                    newc = c + d[1]
                    if in_bound(newr , newc) and image[newr][newc] == or_color:
                        image[newr][newc] = color
                        queue.append((newr , newc))
        return image