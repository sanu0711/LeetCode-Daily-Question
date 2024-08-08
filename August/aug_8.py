# https://leetcode.com/problems/spiral-matrix-iii/description/

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        ans=[]
        dx,dy,n=0,1,0
        while len(ans)<rows*cols:
            for i in range(n//2+1):
                if 0<=rStart<rows and 0<=cStart<cols:
                    ans.append([rStart,cStart])
                rStart=rStart+dx
                cStart=cStart+dy
            dx,dy,n=dy,-dx,n+1
        return ans       
    