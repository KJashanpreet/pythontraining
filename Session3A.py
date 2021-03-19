#List
#also indexed
#            0      1        2      3      4
followers=["john","jannie","leo","jazz","ammy"]

print("followers is: ",followers)
print("type of followers is",type(followers ))
print("followers hashcode is:",hex(id(followers)))
#List is mutable i.e. we can manipulations in the list

followers.append("kia")
followers.append("dave")
print("followers now:", followers)
followers [1]="fionna.flynn"
print("followers now:", followers)

#del followers[1]

print("followers now:",followers)