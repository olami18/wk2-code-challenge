class Review:
    all_reviews = []  

    def __init__(self, customer, restaurant, rating):
        
        if type(rating) != int:
            raise ValueError("Ensure the rating is a number!")
        
        
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        
        self.save_review()

    
    @property
    def review_rating(self):
        return self._rating  
       
    
    @classmethod
    def all(cls):
        return cls.all_reviews  
    
    
    def save_review(self):
        self.all_reviews.append(self) 
    
    
    def review_customer(self):
        return self._customer

    
    def review_restaurant(self):
        return self._restaurant
    def __repr__(self):
        return f"{self._customer}, {self._restaurant}, {self._rating}"




# # Test Instances fpr Class Review
# review1 = Review("Alice Johnson", "Restaurant A", 4)
# review2 = Review("Bob Smith", "Restaurant B", 5)
# review3 = Review("Alice Johnson", "Restaurant A", 3)

# # Get the review rating using the property
# print(f"Review 1 Rating: {review1.review_rating}")

# # Get all reviews using the class method
# all_reviews = Review.all()
# print("All Reviews:")
# for review in all_reviews:
#     print(f"Customer: {review.review_customer()}, Restaurant: {review.review_restaurant()}, Rating: {review.review_rating}")

# # Add a new review
# new_review = Review("Carol Brown", "Restaurant C", 2)

# # Get the updated list of all reviews
# all_reviews = Review.all()
# print("Updated All Reviews:")
# for review in all_reviews:
#     print(f"Customer: {review.review_customer()}, Restaurant: {review.review_restaurant()}, Rating: {review.review_rating}")
