class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_count = {}

        for task in tasks:
            freq_count[task] = freq_count.get(task, 0) + 1
        
        max_freq = max(freq_count.values())
        count_max = 0
        for key, value in freq_count.items():
            if value == max_freq:
                count_max +=1
        return max((max_freq-1) * (n+1) + count_max, len(tasks))