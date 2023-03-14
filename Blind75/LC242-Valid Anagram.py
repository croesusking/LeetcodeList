class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # LC242-Valid Anagram
        dict1 = {}
        dict2 = {}

        for i in s:
            dict1[i] = 1 + dict1.get(i, 0)
        
        for i in t:
            dict2[i] = 1 + dict2.get(i, 0)


        for key1, value1 in dict1.items():
            if key1 not in dict2 or value1!=dict2[key1]:
                return False

        return True if len(dict1)==len(dict2) else False
            