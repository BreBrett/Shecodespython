#boolean
is_raining = True
is_cold = True
print(type(is_raining))
print(type(is_cold))

print(is_raining)
print(not is_raining)
print(is_raining and is_cold)

print(is_raining and is_cold)#True

print(is_raining)
print(not is_raining)
print(is_raining or is_cold)
print(is_raining and not is_cold)
print(is_raining or not is_cold)
print(not is_raining and not is_cold)
print()
temp = 16
print(temp <18)
print(temp >18)

wind_chill = 3
print(wind_chill >4)
print(temp - wind_chill <16)

code = "freeticket"
print (code == "freeticket")
print (code != "freeticket")

is_raining = False
if is_raining:
    print("Take an umbrella")
else:
    print("Do not take an umbrella")

temp = 16
wind_chill = 4

if temp - wind_chill < 16:
    print("Take a jumper.")
elif temp - wind_chill > 30:
    print ("It is hot.Stay home.")
else:
    print ("Wow, what a lovely day!")

if temp <16:
    if is_raining:
        print ("Just stay home.")
    else:
        print("Its ok today.")

moths_in_house = False
mitch_is_home = True 
print(type(moths_in_house and mitch_is_home))

if moths_in_house and mitch_is_home:
    print ("Climb on Mitch.")
else:
    print ("No threats detected")
print()

light_colour =  "Amber"
car_detected =  True
print (type (light_colour and car_detected))

if light_colour == "Red" and not car_detected:
        print ("Do Nothing")
elif light_colour == "Red" and car_detected:
        print ("Flash!")
else:
        print ("Do Nothing")
print()

height = 120

if height >= 120:
    print ("Hop on!")
else:
    print ("Sorry,not today")
