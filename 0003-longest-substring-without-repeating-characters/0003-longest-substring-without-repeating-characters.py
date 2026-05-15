class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0

        for i in range(len(s)):
            substring = ""

            for j in range(i, len(s)):

                if s[j] in substring:
                    break

                substring += s[j]

            maxi = max(maxi, len(substring))

        return maxi