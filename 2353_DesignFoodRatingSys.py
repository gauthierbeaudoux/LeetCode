class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        set_cuisine = set(cuisines)
        self.dic_cuisine = {}
        for i in set_cuisine:
            self.dic_cuisine[i] = []
        
        self.food_rating = {}
        for j in range(len(cuisines)):
            self.dic_cuisine[cuisines[j]].append(foods[j])
            self.food_rating[foods[j]] = ratings[j]
        

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        ratingMax = -1
        for i in self.dic_cuisine[cuisine]:
            if self.food_rating[i] > ratingMax:
                result = i
                ratingMax = self.food_rating[i]
            elif self.food_rating[i] == ratingMax and i < result:
                result = i
                ratingMax = self.food_rating[i]
        return result

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)