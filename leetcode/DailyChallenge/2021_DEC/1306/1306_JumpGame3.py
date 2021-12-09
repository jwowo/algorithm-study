from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        visited = [False] * len(arr)
        
        queue.append(start)
        
        while queue:
            current_idx = queue.popleft()
            visited[current_idx] = True
                
            for i in range(2):
                if i == 0:
                    next_idx = current_idx + arr[current_idx]
                else:
                    next_idx = current_idx - arr[current_idx]
                    
                if 0 <= next_idx < len(arr):
                    if arr[next_idx] == 0:
                        return True
                    
                    if visited[next_idx] == False:
                        queue.append(next_idx)
                    
        return False