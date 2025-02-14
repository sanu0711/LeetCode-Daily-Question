# https://leetcode.com/problems/regions-cut-by-slashes/

class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        parent = {}
        
        # Initialize the union-find parent for each triangle
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        # Each cell is represented by 4 triangles: 0 (top-left), 1 (top-right), 2 (bottom-right), 3 (bottom-left)
        def get_index(i, j, k):
            return (i * n + j) * 4 + k
        
        # Initialize all triangles
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    parent[get_index(i, j, k)] = get_index(i, j, k)
                        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    union(get_index(i, j, 0), get_index(i, j, 3))
                    union(get_index(i, j, 1), get_index(i, j, 2))
                elif grid[i][j] == '\\':
                    union(get_index(i, j, 0), get_index(i, j, 1))
                    union(get_index(i, j, 2), get_index(i, j, 3))
                else:
                    union(get_index(i, j, 0), get_index(i, j, 1))
                    union(get_index(i, j, 1), get_index(i, j, 2))
                    union(get_index(i, j, 2), get_index(i, j, 3))
                
                # Union with right and bottom cells if possible
                if j + 1 < n:
                    union(get_index(i, j, 1), get_index(i, j + 1, 3))
                if i + 1 < n:
                    union(get_index(i, j, 2), get_index(i + 1, j, 0))
        
        # Count the number of distinct roots
        return sum(find(x) == x for x in parent)
        