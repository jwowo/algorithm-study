class Solution:
    def maxPower(self, s: str) -> int:
        max_count = 1
        count = 1
        prev_char = s[0]
        
        for i in range(1, len(s)):
            if prev_char == s[i]:
                count += 1
            else:
                count = 1
            
            prev_char = s[i]
            max_count = max(max_count, count)
            
        return max_count