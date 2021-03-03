ribbon_friend = [ "chinmay", "yashadip", "nithin", "anu" ]
mark_friend = [ "saket", "mandar", "sanket", "swapnil"]

print(mark_friend[1])

del mark_friend[3]

print(mark_friend)

mark_friend.append("swapnil")

print(mark_friend)

mark_friend.insert(1,"ashish")
print(mark_friend)

print(mark_friend.count("mandar"))

mark_friend.reverse()

print(mark_friend)

mark_friend.remove("swapnil")

print(mark_friend)

print(mark_friend + ribbon_friend)