class Solution(object):
    def isValidSudoku(self, board):
        nums =  board

        for i in range(len(nums)):
            if len(nums[i]) != 9:
                return False

        for i in range(9):
            row = [nums[i][j] for j in range(9) if nums[i][j] != '.']
            col = [nums[j][i] for j in range(9) if nums[j][i] != '.']
            
            if not self.check_fun(row) or not self.check_fun(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [nums[x][y] for x in range(i, i+3) for y in range(j, j+3) if nums[x][y] != '.']
                if not self.check_fun(subgrid):
                    return False

        return True

    def check_fun(self, lst):
        seen = set()
        for item in lst:
            if item in seen:
                return False
            seen.add(item)
        return True
