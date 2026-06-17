class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append('#')
            res.append(string)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        start_id = 0
        while start_id < len(s):
            end_id = self.read_number(s, start_id)
            # print(start_id, end_id, s, s[end_id])
            length = int(s[start_id: end_id])
            content = s[end_id+1: end_id+1+length]
            start_id = end_id+1+length
            res.append(content)
        return res

    def read_number(self,s,start):
        end = start
        while s[end].isdigit():
            end+=1
        return end