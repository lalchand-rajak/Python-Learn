rbbn_friend = {
    "chinmay": 80,
    "yashdaip": 80,
    "nithin": 90,
    "sandeep": 90
}

mark_friend = {
    "saket": 80,
    "mandar": 80,
    "swapnil": 80
}

print(rbbn_friend)
print(mark_friend)

print(rbbn_friend.keys())
print(rbbn_friend.values())
print(len(rbbn_friend))

print(len(mark_friend))
print(rbbn_friend.clear())
print(rbbn_friend)
rbbn_friend.update(mark_friend)
# print(rbbn_friend)

myTag = ( "fist_name", "last_name", "age", "phone_no")

myOne = dict.fromkeys(myTag)
print("Dictionary is: %s" %str(myOne))
