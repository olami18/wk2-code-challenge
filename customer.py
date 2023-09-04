from review import Review
class Customer:
    total_customers = [] 
    def __init__(self, given_name, family_name):
        self.given_name = given_name 
        self.family_name = family_name
        self.full_name = self.given_name + " " + self.family_name
        self.__class__.total_customers.append(self) 
   
        
    def get_given_name(self):
        return self.given_name
    
    
    def set_given_name(self, new_name):
        self.given_name = new_name
        self.full_name = self.given_name + " " + self.family_name
        
    
    def get_family_name(self):
        return self.family_name
            
    
    def set_family_name(self, new_name):
        self.family_name = new_name
        self.full_name = self.given_name + " " + self.family_name
    
    
    def get_full_name(self):
        return self.full_name
     
    
    @classmethod
    def all(cls):
        return cls.total_customers
    
    
    def customer_restaurants (self):
       return set([review.review_restaurant() for review in Review.all() if review.review_customer() in self.full_name])
    
        
    def add_review (self, restaurant, rating):
        Review(self.get_full_name(), restaurant, rating)
    
    
    def num_reviews (self):
        reviews = [review for review in Review.all() if review.review_customer() in self.full_name]
        return len(reviews)
    
    
    @classmethod
    def find_by_name (cls, name):
        for customer in cls.customers:
            if customer.full_name() == name:
                return customer
            else: 
                print("Searched customer not accessed")
    
    
    @classmethod
    def find_by_name(cls, name):
      for customer in cls.total_customers:  
        if customer.full_name == name:  
            return customer
        else: 
            print("Searched customer not accessed")
    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = [customer for customer in cls.total_customers if customer.given_name == given_name]
        return matching_customers
    
    def get_reviews(self):
      return [review for review in Review.all() if review.review_customer() in self.full_name]
    
    def __repr__(self):
        return f"{self._family_name}, {self._given_name} "
