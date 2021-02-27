# # score = 20
# score = int(input("enter your score.! "))
# if score < 30:
#     print ("Please try again.!")
# else:
#     print("Great score",score)

feedback = int(input("Give the rating.! "))

if feedback == 5:
    print("Thanks, Visit again")
elif feedback == 0:
    print("sorry, will improve")
else:
    print("Thanks")
