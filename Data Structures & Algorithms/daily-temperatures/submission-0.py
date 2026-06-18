class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Keep a stack, count_tem.
            count_tem[k] is the minimum temperature with k temperature smaller that itself
        the search algorithm is to find the first item larger than current value.
        """
        waiting_tem = []

        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while waiting_tem and waiting_tem[-1][0]<temperatures[i]:
                tem, idx = waiting_tem.pop()
                res[idx] = i-idx
            waiting_tem.append([temperatures[i], i])
        return res 