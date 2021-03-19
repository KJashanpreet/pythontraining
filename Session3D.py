#DICTIONARY also known as MAP or HASHMAP
#store the data as key value pair
restaurant= {
    "name": "Gopal sweet",
    "review": 4.5,
    "Categories": ["Mithai", "Indian", "Bakery", "Fast food"],
    "time to delivered": 35,
    "Price_per_person": 150,
    "promocode": "CRAVINGS25"
}
print( restaurant)
print(type(restaurant))
print(len(restaurant))
restaurant["address"]= "Sarabha Nagar"
restaurant["phone"]="90909 12121"
print( restaurant)
print(type(restaurant))
print(len(restaurant))
dish1= {
     "name": "Gujiya" ,
    "price": 125
}
dish2 = {
  "name":"milk cake" ,
  "price": 150,
}
dish3 = {
    "name": "Khoya burfi" ,
    "price": 180,
}
Dishes=[dish1, dish2, dish3]
restaurant["dishes"]= dishes
print("RESTAURANT")
print(restaurant)
