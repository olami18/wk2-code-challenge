from review import Review
from customer import Customer
from restaurant import Restaurant


customer1 = Customer("Alice", "Johnson")
customer2 = Customer("Bob", "Smith")
customer3 = Customer("Charlie", "Brown")


print("All Customers:")
for customer in Customer.all():
    print(customer.get_full_name())


customer1.add_review("Restaurant A", 4)
customer2.add_review("Restaurant B", 5)
customer3.add_review("Restaurant C", 3)


print("Reviews by customer1:")
for review in customer1.get_reviews():
    print(review)
print("Reviews by customer2:")
for review in customer2.get_reviews():
    print(review)
    
print("Reviews by customer3:")
for review in customer3.get_reviews():
    print(review)



print("\nCustomer Restaurants:")
for customer in Customer.all():
    print(f"{customer.get_full_name()}: {customer.customer_restaurants()}")


print("\nNumber of Reviews:")
for customer in Customer.all():
    print(f"{customer.get_full_name()}: {customer.num_reviews()}")


found_customer = Customer.find_by_name("Alice Johnson")
if found_customer:
    print(f"Found Customer: {found_customer.get_full_name()}")
else:
    print("Customer not found.")


customers_with_name = Customer.find_all_by_given_name("Alice")
print("\nCustomers with Given Name:")
for customer in customers_with_name:
    print(customer.get_full_name())




restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")


print(f"Restaurant Name: {restaurant1.rest_name()}")
print(f"Reviews: {restaurant1.restaurant_reviews()}")
print(f"Customers: {restaurant1.restaurant_customers()}")
print(f"Average Rating: {restaurant1.average_star_rating()}")

print("-" * 20)

print(f"Restaurant Name: {restaurant2.rest_name()}")
print(f"Reviews: {restaurant2.restaurant_reviews()}")
print(f"Customers: {restaurant2.restaurant_customers()}")
print(f"Average Rating: {restaurant2.average_star_rating()}")



review1 = Review("Alice Johnson", "Restaurant A", 4)
review2 = Review("Bob Smith", "Restaurant B", 5)
review3 = Review("Alice Johnson", "Restaurant A", 3)


print(f"Review 1 Rating: {review1.review_rating}")


all_reviews = Review.all()
print("All Reviews:")
for review in all_reviews:
    print(f"Customer: {review.review_customer()}, Restaurant: {review.review_restaurant()}, Rating: {review.review_rating}")


new_review = Review("Carol Brown", "Restaurant C", 2)


all_reviews = Review.all()
print("Updated All Reviews:")
for review in all_reviews:
    print(f"Customer: {review.review_customer()}, Restaurant: {review.review_restaurant()}, Rating: {review.review_rating}")
