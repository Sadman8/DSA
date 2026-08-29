class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        m_len= 0
        start =0
        for end in range(len(s)):
            if s[end] in dic:
                start = max(start, dic[s[end]]+1)
            dic[s[end]]=end
            m_len = max(m_len , end - start + 1)

        return m_len