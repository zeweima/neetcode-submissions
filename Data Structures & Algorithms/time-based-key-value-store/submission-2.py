class TimeMap:

    def __init__(self):
        self.key_value = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value[key] = self.key_value.get(key, [])
        self.key_value[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_value:
            return ""
        values = self.key_value[key]

        l, r = 0, len(values)-1
        while l<=r:
            mid = (l+r)//2

            if values[mid][0]<=timestamp:
                l = mid + 1
            else:
                r = mid -1
        if l==0:
            return ''
        return values[l-1][1]
        
