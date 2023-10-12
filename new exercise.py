print("Welcome to this new challenge")
height= int(input("What is your height in cm?"))

if height >= 120:
    print("Hurray! You can take a ride now")
    age= int(input("What is your age?"))
    if age <12:
        print("Children tickets are $5")
    elif age <=18:
        print("Teenagers tickets are $7")
    else:
        print("Adult tickets are $12")
    
else:
    print("Oops! Try again later")

    
print("Welcome to this new challenge")
height= int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("Hurray! You can take a ride now")
    age= int(input("What is your age?"))
    if age <12:
        bill = 5
        print("Children tickets are $5")
    elif age <=18:
        bill = 7
        print("Teenagers tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    photo_taken = input("Do you want to take photos? Y or N")
    if photo_taken == "Y":
        bill = bill + 3
    print (f"Your final bill is ${bill}")
else:
    print("Oops! Try again later")




Pizza Order
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size =="S":
    bill =15
elif size =="M":
    bill = 20
else:
    bill = 25

if add_pepperoni =="Y":
    if size =="S":
        bill = bill + 2
    else:
        bill = bill + 3

if extra_cheese == "Y":
    bill = bill +1

print(f"Your final bill is: ${bill}.")



