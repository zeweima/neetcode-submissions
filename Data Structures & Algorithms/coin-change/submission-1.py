class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount == 0:
        #     return 0
        # min_amount = [0] * (amount+1)

        # min_amount[0] = 1
        
        # n_count = 1
        # valid=True
        # while valid:
        #     valid = False
        #     for i in range(amount,-1,-1):
        #         if min_amount[i]==n_count:
        #             valid = True
        #             for coin in coins:
        #                 if i+coin==amount:
        #                     return n_count
        #                 if i+coin<=amount:
        #                     min_amount[i+coin] = n_count+1
        #     # print(min_amount)
        #     n_count = n_count+1
        # return -1

        min_count = [float('inf')]*(amount+1)
        min_count[0] = 0

        for a in range(1,amount+1):
            for coin in coins:
                if a-coin>=0:
                    min_count[a] = min(min_count[a], min_count[a-coin]+1)
        return min_count[-1] if min_count[-1]<float('inf') else -1