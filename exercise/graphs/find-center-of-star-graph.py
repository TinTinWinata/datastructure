class Solution(object):
    def findCenter(self, edges):
        most = {}
        most_number = [0, 0]
        for edge in edges:
            for node in edge:
                if node in most:
                    most[node] += 1
                else:
                    most[node] = 1
                if most[node] > most_number[0]:
                    most_number[1] = node
                    most_number[0] = most[node]
        return most_number[1]

s = Solution()
# print(s.findCenter([[1,2],[2,3],[4,2]]))
print(s.findCenter([[1,2],[5,1],[1,3],[1,4]]))