class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        l = 0 
        maxLen = 0
        
        for r in range(len(s)):
            chars[s[r]] += 1
            
            window_size = r - l + 1
            
            if window_size - max(chars.values()) <= k:
                maxLen = max(maxLen, window_size)
            else:
                chars[s[l]] -= 1

                if not chars[s[l]]:
                    del chars[s[l]]
                l += 1
            
        return maxLen
