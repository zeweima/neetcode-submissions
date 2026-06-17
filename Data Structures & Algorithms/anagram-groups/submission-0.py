class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        res_dict = defaultdict(list)
        for word in strs:
            sort_word = ''.join(sorted(word))
            # print(sort_word)
            res_dict[sort_word].append(word)
        return list(res_dict.values())