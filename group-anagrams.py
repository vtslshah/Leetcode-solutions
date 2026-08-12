class Solution:
    def groupAnagrams(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        
        anagramlist = {}
        for str in strs:
            sortedString = "".join(sorted(str))
            if not anagramlist.get(sortedString,''):
                anagramlist[sortedString] = []

            anagramlist[sortedString].append(str)
            
        print(anagramlist.values())

obj = Solution()
obj.groupAnagrams()