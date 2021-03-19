name1 = "john"
name2 = "john"
print(name1,type(name1),hex(id(name1)))
print(name2,type(name2),hex(id(name2)))
followers={"john","jannie","leo","jazz","ammy"}
print("folllowers is:",followers)
print("type of followers is:" ,type(followers))
print("followers hashcode is:",hex(id(followers)))
followers.add("kia")
followers.add("dave")
followers.add("fionna")
followers.add("john")
print("followers now:",followers)
print("total followers:",len(followers))