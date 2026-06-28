class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        meet = set()

        for a, b, c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            
            if a==target[0]:
                meet.add(0)
            if b==target[1]:
                meet.add(1)
            if c==target[2]:
                meet.add(2)
        
        if len(meet)==3:
            return True
        return False