class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #Sets for the validation
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqr = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                current = board[r][c] #get the current cell

                if current == '.':
                    continue

                #check the value for every set
                if current in rows[r]:
                    return False
                rows[r].add(current)

                if current in cols[c]:
                    return False
                cols[c].add(current)

                if current in sqr[(r//3)*3+(c//3)]:
                    return False
                sqr[(r//3)*3+(c//3)].add(current)
                
        return True