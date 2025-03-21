from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        for recipe, ingredient_list in zip(recipes, ingredients):
            for ingredient in ingredient_list:
                graph[ingredient].append(recipe)
                in_degree[recipe] += 1
        
        queue = deque(supplies)
        result = []
        
        while queue:
            item = queue.popleft()
            
            if item in recipes:
                result.append(item)
            
            for neighbor in graph[item]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result

print(Solution().findAllRecipes(["bread", "sandwich", "burger"], [["flour", "water"], ["bread", "meat"], ["sandwich", "lettuce"]], ["flour", "water", "meat", "lettuce"]))  # Output: ["bread", "sandwich", "burger"]
