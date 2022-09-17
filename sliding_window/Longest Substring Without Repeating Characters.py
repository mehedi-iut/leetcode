s = "abcabcbb"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bucket = set()
        max_len = 0
        start, end = 0, 0

        while end < len(s):
            if s[end] not in bucket:
                bucket.add(s[end])
                end += 1
            
            else:
                while s[end] in bucket:
                    bucket.remove(s[start])
                    start += 1
            
            max_len = max(max_len, len(bucket))
        return max_len

sln = Solution()
print(sln.lengthOfLongestSubstring(s))