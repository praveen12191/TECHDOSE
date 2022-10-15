from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        self.has = defaultdict(SortedList)
        self.food = {}
        for x,y,z in zip(foods,cuisines,ratings):
            self.has[y].add((-z,x))
            self.food[x] = [y,z]
        
    def changeRating(self, food: str, newRating: int) -> None:
        x,y = self.food[food]
        self.food[food] = x,newRating
        self.has[x].remove((-y,food))
        self.has[x].add((-newRating,food))
    def highestRated(self, cuisine: str) -> str:
        return self.has[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)