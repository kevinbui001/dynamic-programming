import sys
from typing import List
import unittest


class Solution:
    def min_cost_tickets(self, grid: List[List[int]]) -> int:
        # dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]
        # initalize dp
        dp = [[sys.maxsize for j in range(len(grid[0]))]
              for i in range(len(grid))]
        # assing first dp (0,0) to grid (0,0)

        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # skip the first one
                if i + j == 0:
                    continue
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


s = Solution()

m = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]


class MyTest(unittest.TestCase):

    def test_true(self):
        self.assertTrue(True)

    def test_equal(self):
        self.assertEqual(s.min_cost_tickets(m), 7)


def main():
    print("---- RUNNING MAIN ----")
    print(s.min_cost_tickets(m))
    print("---- DONE MAIN ----\n\n")


# Main body
if __name__ == '__main__':
    main()
    unittest.main()
