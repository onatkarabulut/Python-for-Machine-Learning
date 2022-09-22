# Chapter 1
### Your first day at your new job 👩‍💻👨‍💻

# You are starting a new job as a junior software developer in an IT company. 

# The company’s HR department asks you to fill out a form, so you start by assigning your personal information to corresponding variables.

# 📌 Create a variable for your name, surname, age, ID number, place of residence, to specify if you have active health insurance or not, and lastly one for specifying your nationality.

#Please assign your personal information to variables
my_name='Onat'
my_surname='Karabulut'
my_age=18
ID_number=12874
where_i_live='Ankara'
health_insurance=False
###Meet And Greet
# Introduce yourself to your new co-workers.

# 📌 Use a f-string to print "My name is Joey Tribbiani I am 25 years old and I live in London”.
#Write a sentence using the print function to describe yourself using the variables above in the correct data type
print(f"My name is {my_name} {my_surname}.I am {my_age} years old. I live in {where_i_live}.")
### Equipment starter pack
# The HR department asks you to list the items you would need to improve your work efficiency

# Mandatory:
# * Laptop
# * Headset
# * Second monitor

# Optional:
# * Mousepad
# * USB drive
# * External drive


# 📌 Create a shopping list that contains items above and print it.
#Create the item_list
item_list=['Laptop','Headset','Second Monitor','Mousepad','USB drive','External drive']
#Print the list
print(item_list)
####What is mandatory and what is optional?

# 📌 Use list slicing to devide your list in two list: 'mandatory_item_list' and 'optional_item_list' and print both to the screen.
#Use list slicing to divide the mandatory items
mandatory_items=item_list[0:3]
#Use list slicing to divide the optional items
optional_items=item_list[3:]
#Print both to the screen
print(mandatory_items)
print(optional_items)
#### Go Shopping
# Next, you will have to go and purchase these items, the finance department confirmed a budget of $5000.

# 📌 Assign 5000 to a variable called limit, so you know how much you can spend.
#Assign the spending limit value to a variable called limit
limit=5000
####Price dictionary

# Before you start shopping yo need to find the best items that you can buy within the company budget. 

# 📌 Prepare a dictionary called “price_sheet” that includes the items as keys and the prices as values.  
 
#Create a dictionary that contains each item and its price

price_sheet={'Laptop':1500,
            'Headset':100,
            'Second Monitor':500,
            'Mousepad':30,
             'USB drive':50,
             'External drive':500
            }
####Shopping functions

# You need to define three functions that will help you during shopping.

# 📌 First, create an empty list that  will be your shopping cart. Here you will add the items you need to purchase.

# 1. Define a function for both adding items to the cart and removing them from the item_list.

# 📌 The "add_to_cart" function should take the item name and the quantity to buy as an argument. 

# 2. Define a function that will create an invoice. 

# 📌 The "create_invoice" function should calculate the taxes of each item (18%) and add it to the total amount.

# 3. Define a function for the checkout. 

# 📌 The "checkout" function should subtract the total amount from the budget and print a statement to inform if the payment was successful. 
#Initialize the cart list
cart=[]
#Define the "add_to_cart" function
def add_to_cart(item,quantity):
    cart.append((item,quantity))
    item_list.remove(item)
#Define the "create_invoice" function
def create_invoice():
    total_amt_inc_tax=0
    for item,quantity in cart:
        price=price_sheet[item]
        total=((0.18*price)+price)*quantity
        total_amt_inc_tax+=total
        print('Item:',item,'\t','Price:',price,'\t','Quantity:',quantity,'\t','Total:',total,'\n')
        
    print('After the taxes are applied the total amount is:',total_amt_inc_tax)
    return total_amt_inc_tax
#Define the "checkout" function
def checkout():
    global limit
    total_amount=create_invoice()
    if limit==0:
        print("You don't have any budget." )
    elif total_amount>limit:
        print("The amount you have to pay is above the spending limit. Drop some items.")
    else:
        print("Payment successful")
    
# Let's shop!
#Call the "add_to_cart" function for each item
 
#Add first item to cart
add_to_cart('Laptop',1)
 
#Add second item to cart
add_to_cart('Headset',3)
 
#Add third item to cart
add_to_cart('Second Monitor',2)
 
#Add fourth item to cart
add_to_cart('Mousepad',2)
 
#Add fifth item to cart
add_to_cart('USB drive',1)
 
#Add last item to cart
add_to_cart('External drive',1)
 
#Call the create "checkout" function to pay for all your items 
checkout()
###Game Night

# You are back at the office and the HR department organizes a welcome party for new employees. 

# You decide to create a Rock-Paper-Scissor game. 

# 📌 Create a Rock-Paper-Scissor game in which the user plays against the computer. The player will choose one of the actions, and the computer will choose its action randomly.

#Import the random library
import random
#create a list containing the three actions of the game.
action_list=['rock','paper','scissors']
#Set the scores of players to 0
player=0
computer=0

#Ask the user how many rounds they want to play
total_rounds=input("How many rounds would you like to play?\n")

#Add a round_counter that is 0 at the beginning
round_counter=0

#Write a while loop and put the game inside
while True:

    #Increase round_counter by and print it
    round_counter+=1
    print("Round number:",round_counter)  


  #Select a random action for computer
    computer_choice=random.choice(action_list)

  #Ask player to choose an action
    player_choice=input("Enter your action.")

  #Print the players choices
    print("Computer choose:",computer_choice)
    print("You choose:",player_choice)



  #tie condition
    if(computer_choice==player_choice):
        print("Its a tie.")
        player+=1
        computer+=1


  #Remaining conditions
    elif(computer_choice=='rock'):
        if(player_choice=='paper'):
            print("Victory!")
            player+=1
        else:
            print("Defeat.")
            computer+=1
    
    elif(computer_choice=='paper'):
        if(player_choice=='scissors'):
            print("Victory!")
            player+=1
        else:
            print("Defeat.")
            computer+=1
    elif(computer_choice=='scissors'):
        if(player_choice=='rock'):
            print("Victory!")
            player+=1
        else:
            print("Defeat.")
            computer+=1





  #Stop the while loop if the round_counter equals the number of total rounds
    if round_counter==int(total_rounds):
         break


#Print the outcome of the game by using conditional statements
if computer==player:
    print(f"There is no winner.\nYour Score:{player}\nCPU score:{computer}")
elif computer>player:
    print(f"You lose.\nYour Score:{player}\nCPU score:{computer}")
else:
    print(f"You Win.\nYour Score:{player}\nCPU score:{computer}")
# Your first task 

# Rachel asks you to write a program to track the name and revenue each employee brings.  

# * Create the "salesperson_revenue" dictionary to see the employee name as a key and the revenue as a value.

#   📌 Every employee starts with 0 revenue.
# * Define the "enter_revenue" function. 

#   📌 The function takes the name and revenue as an argument and updates the salesperson_revenue dictionary.

#Create salesperson_revenue dictionary
salesperson_revenue={'Sumit':0,
                    'Ram':0,
                    'Harry':0,
                    'Sam':0,
                    'Rose':0,
                    'Romeo':0,
                    'Krishna':0,
                    'Ben':0}
#Define enter_revenue function
def enter_revenue(name,revenue):
    global salesperson_revenue
    salesperson_revenue[name]+=revenue
    

####Try out the functions
# * In a while loop ask the user to give the name of the employee and for the revenue 

#   📌 If the user enters “quit” the loop should break.

# After that, print out the salesperson_revenue dictionary.

#Asking user employee name as input
while True:
    name=input("Enter Employee name:")
    if name=='quit':
        break
    revenue=int(input("Enter revenue:"))
    enter_revenue(name,revenue)
    print(f"{name}'s revenue is {salesperson_revenue[name]}")
#Print the salesperson_revenue dictionary
print(salesperson_revenue)