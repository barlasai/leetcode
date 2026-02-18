class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0 for j in range(n)]for i in range(n)]
        ele=[i for i in range(1,n*n+1)]
        k=0
        top,bottom = 0,n-1
        left,right = 0,n-1
        while (top <= bottom) and (left <= right):
            #left to right
            for i in range(left,right+1):
                matrix[top][i]=ele[k]
                k+=1
            top+=1

            #top to bottom
            for i in range(top,bottom+1):
                matrix[i][right]=ele[k]
                k+=1
            right-=1

            #right to left
            if top <= bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=ele[k]
                    k+=1
                bottom-=1

            #bottom to top
            if left <= right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left]=ele[k]
                    k+=1
                left+=1
        return matrix
                    

        