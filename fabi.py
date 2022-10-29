class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        max = -1
        for i in range(len(strs[0]) + 1):
            for cuv in strs:
                if strs[0][:i] not in cuv[:i]:
                    break
            else:
                if len(strs[0][:i]) > max:
                    max = len(strs[0][:i])
                    prefix = strs[0][:i]
        return prefix
