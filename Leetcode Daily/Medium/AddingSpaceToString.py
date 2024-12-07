from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []                   # Use a list for efficient string construction
        it = 0                        # Pointer for spaces array

        for i, char in enumerate(s):
            if it < len(spaces) and i == spaces[it]: # Insert space if index matches
                result.append(' ')
                it += 1
            result.append(char)       # Append character to result

        return ''.join(result)        # Combine list into final string