class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        change_position = [0, 0]
        for count in position:
            if count % 2 == 0:
                change_position[0] += 1
            else:
                change_position[1] += 1
                
        return min(change_position)