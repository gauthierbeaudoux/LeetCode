heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2

def furthestBuilding(heights: list[int], bricks: int, ladders: int) -> int:
    def dp(height, brick, ladder, colonne):
        if colonne == len(height)-1:
            return 0
        if height[colonne+1] <= height[colonne]:
            return 1+dp(height,brick,ladder,colonne+1)
        distance_brick = 0
        distance_echelle = 0
        if height[colonne+1] - height[colonne] <= brick:
            distance_brick = 1+dp(height,brick-(height[colonne+1] - height[colonne]),ladder,colonne+1)
        if ladder > 0:
            distance_echelle = 1+dp(height,brick,ladder-1,colonne+1)
        
        return max(distance_brick, distance_echelle)

    return dp(heights, bricks, ladders, 0)

print(furthestBuilding(heights, bricks, ladders))

