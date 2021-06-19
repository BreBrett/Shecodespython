chilli_wishlist = [ 
    "igloo",
    "chicken",
    "donut toy",
    "cardboard box",
]
print(chilli_wishlist)
print(chilli_wishlist [0])
print (len(chilli_wishlist))
print (chilli_wishlist[-1])
print (chilli_wishlist[0:2])
chilli_wishlist[1] = "carrot"
print(chilli_wishlist)
print (chilli_wishlist [2:3])
print (chilli_wishlist [-3])

chilli_wishlist.append('dig mat')
print (chilli_wishlist)
chilli_wishlist.extend(["kong","crocodile toy"])
print (chilli_wishlist)
chilli_wishlist.insert(1,"peanut butter")
print(chilli_wishlist)

#remove items 
print(chilli_wishlist.pop())
print(chilli_wishlist)
print(chilli_wishlist.pop(2))
print (chilli_wishlist)
chilli_wishlist.remove("kong")
print(chilli_wishlist)
chilli_wishlist.insert(-2,"bone")
print(chilli_wishlist)
chilli_wishlist.remove("donut toy")
print(chilli_wishlist)
chilli_wishlist.extend(["mouse","cheese","lamb chops","cats"])
print (chilli_wishlist)
print()
chilli_wishlist = [
    ["igloo"], # bed
    ["donut toy", "tennis ball","croodile"],
    ["chicken","peanut butter"], # treats
    ["cardboard box","kong"] # puzzles 
]
print(chilli_wishlist)
print (chilli_wishlist [0][0])
print (chilli_wishlist [3][0])

foods = [
      "orange",
      "apple",
      "banana",
      "strawberry",
      "grape",
      "blueberry",
      ["carrot", "cauliflower", "pumpkin"],
      "passionfruit",
      "mango",
      "kiwifruit"
]
print (foods)
