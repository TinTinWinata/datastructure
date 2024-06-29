class Solution(object):
    def maximumImportance(self, n, roads):
        degree = [0] * n
        
        # Calculate the degree of each city
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        print('Degree : ', degree)

        # Create a list of cities and sort by degree
        cities = list(range(n))
        print('Cities : ', cities)
        cities.sort(key=lambda x: -degree[x])
        print('After Sorted Cities : ', cities)
        
        # Assign values to cities starting from the highest degree
        total_importance = 0
        for i in range(n):
            total_importance += (n - i) * degree[cities[i]]
        
        return total_importance
    
s = Solution()
print(s.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])) # 43

print(range(5))