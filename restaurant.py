from review import Review

class Restaurant:
    
    def __init__ (self, restaurant_name):
        self._restaurant_name = restaurant_name        
    
  
    
    def rest_name(self):
        return self._restaurant_name
   
    def restaurant_reviews(self):
       
        return [review for review in Review.all() if review.review_restaurant()== self._restaurant_name]
    
    def restaurant_customers(self):
        
        return set([review.review_customer() for review in self.restaurant_reviews()])
    
    def average_star_rating(self):
    
        allreviews = self.restaurant_reviews()
        
        if len(allreviews) == 0:
            return "No reviews yet."
        
        total_ratings = sum(review.review_rating for review in allreviews)
        
        average_rating = total_ratings / len(allreviews)
        return average_rating





# # Test Instances
# review1 = Review("Alice Johnson", "Restaurant A", 4)
# review2 = Review("Bob Smith", "Restaurant A", 5)
# review3 = Review("Alice Johnson", "Restaurant B", 3)

# # Create Restaurant instances
# restaurant1 = Restaurant("Restaurant A")
# restaurant2 = Restaurant("Restaurant B")

# # Print restaurant information
# print(f"Restaurant Name: {restaurant1.rest_name()}")
# print(f"Reviews: {restaurant1.restaurant_reviews()}")
# print(f"Customers: {restaurant1.restaurant_customers()}")
# print(f"Average Rating: {restaurant1.average_star_rating()}")

# print("-" * 20)

# print(f"Restaurant Name: {restaurant2.rest_name()}")
# print(f"Reviews: {restaurant2.restaurant_reviews()}")
# print(f"Customers: {restaurant2.restaurant_customers()}")
# print(f"Average Rating: {restaurant2.average_star_rating()}")
