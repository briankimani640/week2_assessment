cars = ["jeep", "suv", "sedan"]
car_name = input("Enter the car name : ").lower()
if car_name in cars:
    print(f"We have that car type!")
else:
    print("Sorry, not available.")