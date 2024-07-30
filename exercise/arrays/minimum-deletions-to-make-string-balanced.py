from collections import deque

class Solution:
    def minimumDeletions(self, s: str) -> int:
        if len(s) == 1:
            return 0
        if len(s) == 2:
            return 1 if s[0] == 'b' else 0 
        prefixCountB = [] 
        suffixCountA  = deque()
        countB = 0
        countA = 0
        mountainCount = 0
        peakMountain = float('-inf')
        peakMountainIndex = -1
        for i, v in enumerate(s):
            if v == 'b':
                countB += 1
                mountainCount -= 1
            else:
                mountainCount += 1
            if mountainCount >= peakMountain:
                peakMountain = mountainCount
                peakMountainIndex = i
            prefixCountB.append(countB)
        for v in reversed(s):
            if v == 'a':
                countA += 1
            suffixCountA.appendleft(countA)
        # print('Prefix Count B : ', prefixCountB)
        # print('Suffix Count A : ', suffixCountA)
        # print('Peak Mountain : ', peakMountain)
        # print('Peak Mountain Index : ', peakMountainIndex)
        if suffixCountA[0] == len(s) or prefixCountB[len(s) - 1] == len(s):
            return 0
        if peakMountainIndex == len(s) - 1:
            return prefixCountB[peakMountainIndex]
        if peakMountainIndex == 0:
            return suffixCountA[peakMountainIndex + 1]
        return prefixCountB[peakMountainIndex] + suffixCountA[peakMountainIndex + 1]

# print(Solution().minimumDeletions("aababbab"))
# print(Solution().minimumDeletions("aaaaaaaaaaaaaa"))
# print(Solution().minimumDeletions("aaaaaabbbbabaaaabbabaaabbabbbaaabababaaaaaaabbaaabaaababaaabababa"))
print(Solution().minimumDeletions
      ("bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba"))
# print(Solution().minimumDeletions("bbaaaaaaabbb"))
# print(Solution().minimumDeletions("ba"))
# print(Solution().minimumDeletions("a"))
# print(Solution().minimumDeletions("bab"))
