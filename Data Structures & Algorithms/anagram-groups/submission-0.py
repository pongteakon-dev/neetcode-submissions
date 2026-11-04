from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Instantiate a hashmap
        seen = defaultdict(list)
        # Loop through all strings
        for word in strs:
            # Create a key for sorted words e.g. ate -> aet, tea -> aet
            key = ''.join(sorted(word))
            # add the word value to the sorted key
            seen[key].append(word)
        return list(seen.values())