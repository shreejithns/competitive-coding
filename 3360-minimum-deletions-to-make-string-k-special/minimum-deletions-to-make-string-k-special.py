class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        count = Counter(word)
        res = float('inf')
        for targetFreq in count.values():
            deletions = 0
            for freq in count.values():
                if freq < targetFreq:
                    # delete all characters with frequency less than target
                    deletions += freq
                elif freq > targetFreq + k:
                    # keep only targetFreq + k characters, delete the rest
                    deletions += freq - (targetFreq + k)
                # If targetFreq <= freq <= targetFreq + k, no deletions needed
            res = min(deletions, res)
        return res