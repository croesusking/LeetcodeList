class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #LC 49 - Group Anagrams
        co = collections.defaultdict(list)

        for s in strs:
            dict1 = [0 for _ in range(26)]
            for c in s:
                dict1[ord(c) - ord('a')] +=1

            
            co[tuple(dict1)].append(s)

        return co.values()
