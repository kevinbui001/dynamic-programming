import sys
from typing import List
import unittest


class Solution:
    def min_cost_tickets(self, days: List[int], costs: List[int]) -> int:
        # this is for constant lookup instead of i.e if i in days
        is_travel = [False if not i in days else True for i in range(366)]

        dp = [sys.maxsize for i in range(366)]
        dp[0] = 0

        for i in range(1, 366):
            if not is_travel[i]:  # if not travel day
                dp[i] = dp[i-1]
            else:
                # case 1, one day pass
                dp[i] = min(dp[i], dp[i-1] + costs[0])

                # case 2, week  pass
                if i - 7 >= 0:
                    dp[i] = min(dp[i], dp[i-7] + costs[1])
                # we can still by a week pass for the first 1..6 day if it is less than dp[i]
                else:
                    dp[i] = min(dp[i], costs[1])

                # month pass
                if i - 30 >= 0:
                    dp[i] = min(dp[i], dp[i-30] + costs[2])
                # we can still by a month pass for the first 1..29 day if it is less than dp[i]
                else:
                    dp[i] = min(dp[i], costs[2])

        return dp[365]


s = Solution()

days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
days2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
costs2 = [2, 7, 15]


class MyTest(unittest.TestCase):

    def test_true(self):
        self.assertTrue(True)

    def test_equal(self):
        self.assertEqual(s.min_cost_tickets(days, costs), 11)

    def test_equal2(self):
        self.assertEqual(s.min_cost_tickets(days2, costs2), 17)


def main():
    print("---- RUNNING MAIN ----")
    print(s.min_cost_tickets(days, costs))
    print(s.min_cost_tickets(days2, costs2))
    print("---- DONE MAIN ----\n\n")


# Main body
if __name__ == '__main__':
    main()
    unittest.main()
