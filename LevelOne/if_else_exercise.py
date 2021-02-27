user_rating = int(input("Give the rating B/W 1-5: "))

if user_rating == 1:
    print("Sorry to hear about your experience")
elif user_rating == 2:
    print("we are trying to get better")
elif user_rating == 3:
    print("Thanks")
elif user_rating == 4:
    print("we are almost miss the full rating")
elif user_rating == 5:
    print("Happy to know you love our service")
else:
    print("Please provide rating B/W 1-5")