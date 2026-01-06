class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        
        count = Counter(tiles)
        
        def backtrack():
            total = 0
            for c in count:
                if count[c] > 0:
                    # Use this character
                    total += 1
                    count[c] -= 1
                    # Continue building sequences
                    total += backtrack()
                    # Backtrack
                    count[c] += 1
            return total
        
        return backtrack()