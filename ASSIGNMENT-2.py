print("Welcome to python")
#welcomes the user to python 

name = input("How may i call you?: ")
#asks user to input his name 

print("Welcome to Assingnment 2 ", name)
#Welcomes users to the assignment

print("Hope you like my work, Please go ahead and select the Operator")
#This is just an appreciation message

#float is used to add decimal integer values to the code
#input helps to add input in the code
#for loop runs a loop for specific conditions stated
#while loop runs a loop for specific condition stated




def modulo_calc():
#The above code Defines modulo_calc function which gives moduluos of the entered values

    x = float(input("Enter first number or dividend : "))
    y = float(input("Enter second number or divisor :"))
#x and y are used as input to ask user for nummeric values

    z = x % y
#z is the modulos value of x and y by mathematical function declared as z's value

    print("The Result of",x,"%",y, " is ",z)
#above statement will print the result and values




def int_division_Calc():
#this statement defines the integer dvision function 

    x = float(input("Enter first number or dividend: "))
    y = float(input("Enter second number or divisor: "))
#x ask for the number to be divided and y asks for the number which divides 

    z = x/y
#z= x/y is mathematical Equation for Division

    print("The Result of Division is ",z)
#print statment prints the result of division




def for_loop_count():
#this Statement defines the for loop function
#this function asks user for an input and then increments it or decreases it as per user

    counter = float(input("Enter the Initial Value of counter?"))
#IT asks user for a input of initial value

    loopCount = int(input("How many times you will like the loop to run?"))
#it asks user for loop count 
    
    Increment_i = float(input("Enter the value of Increment ?"))
#it asks user for the value for inncrement

    positive_negative = input("Do you want decrement instead of incrementing? y / n ") == 'n'
#it is asks user if they want a declining loop or inclining loop
    
    if not positive_negative:
        Increment_i = Increment_i * -1
#the above part runs user interpreted data and gives a desired output 
    
    for i in range(loopCount):
#the for loop runs the loop of inncrement/ decrement
        
    
        counter += Increment_i
#this statement increments the initial value until requested
        
    print("The Resulted value of the counter is: ",counter)
#this statement Prints the final resulted of the loop




def float_int_calc():
#this defines the float integer calculator function
    
    def add(x, y):
        return x + y
#this defines addition  function which add 2 digits
    
    def subtract(x, y):
        return x - y
#this defines subtraction function and does subtraction

    def multiply(x, y):
        return x * y
#this function defines multiplication and does multipliction

    def divide(x, y):
        return x // y
#this function defines Division and performs division

    def modulo(x, y):
        return x % y
#this function defines Modulos and gives modulos of the division


    num_1 = float(input("Please Enter  the first number: "))
    num_2 = float(input("Please Enter the second number: "))
#num_1 and num_2 takes the user input for The calculator Function


    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo Calculator")
# The above print Statements gives option to user for performinng his desired Function

    user_choice = input("Select your choice from 1 to 5: ")


    if user_choice == '1':
        print("The Addition of ",num_1, "and", num_2, "is:", add(num_1, num_2))
#the abovecode lines performs addition if user Selects 1
        
    elif user_choice == '2':
        print("The Subraction of ",num_2, "from", num_1, "is:", subtract(num_1, num_2))
#the abovecode lines performs Subtraction if user Selects 2
        
    elif user_choice == '3':
        print("The Multiplication of ",num_1, "and", num_2, "is:", multiply(num_1, num_2))
#the abovecode lines performs Multiplication if user Selects 3
        
    elif user_choice == '4':
        print("The Division of ",num_1, "by", num_2, "is:", divide(num_1, num_2))
#the abovecode lines performs Division if user Selects 4
        
    elif user_choice == '5':
        print("The Modulos of ",num_1, "divided by ", num_2, "is:", modulo(num_1, num_2))
#the abovecode lines performs Modulo if user Selects 5
        
    else:
        print("The Program has Limitations,sorry")
#the above code lines apolozies for not having a interpretation to perform his desired Calculation. 
    



def ASCII_values_display():
#the Above statement Defines ASCII value function
    #this function takes a char and return its ASCII value
    
    str = input("Which String you will like to see the ASCII value of? ")
#The above part will Ask user for a String to display its ASCII value character by character

    strSize = len(str)
    i = 0
#the above codes define i's value and calls for length function
    
    while i < strSize:
        ASCIIvalue = ord(str[i])
#the above code calls ord function and separates the string char by char and defines it ASCII value
        
        print("The character at", i, "is", str[i], "and its ASCII value is",ASCIIvalue)
        i += 1
#the above code Calls for the print function and  and displays the ASCII values character by character until the string ends




def change_machine():
#this defines change machine function
    
     cost = float(input("Please Enter the cost of the product: "))
#here the user inputs the orignal cost of product
     
     amount_paid = float (input("PLease Enter the amount paid by the customer: "))
#here the usewr inputs the amount paid by the customer
     
     change = amount_paid - cost
#Change is calculated by subtracting cost from the amount paid
     

     coins = {
         "quarters": .25,
         "dimes": .10,
         "nickels": .5,
         "pennies": .1
     }
#coins library is created with initial values of the coins

     change_count = {
         "quarters": 0,
         "dimes": 0,
         "nickels": 0,
         "pennies": 0
     }
#Change count library is created for updating the Change value as per coins

     for i in coins:
         while change >= coins[i]:
             change -= coins[i]
             change_count[i] += 1
#for and while loop  are working togather here for calculating the change count

     print("The Change to be Returned is :")
#print statement is given for final outcome
     
     for i in change_count:
         if change_count[i] > 0:
             print(change_count[i],i)
#the above statements calculate value of i and updates change count library and prints the outcome
             


import random
#The above code lines call in the random function 

def rock_paper_scissors_choices(choice):
#the above code lines defines the choices part for the user

    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
    else:
        return None
#the above if else statement  is stated to give user choice for rock ,paper and scissors

def rock_paper_scissors():
    choice = 0
#rock paper scissors function is defined and values of choices by default is set to 0
    
    while choice < 1 or choice > 3:
        choice = int(input("Select your move sir:\n 1.Rock\n 2.Paper\n 3.Scisors\n"))
#while statement is entered to validate user's choice and run the above function 
        
    random.seed() 
    random_number = random.randint(0, 29)
    comp_choice = (random_number + 10) // 10
    computer_output = rock_paper_scissors_choices(comp_choice)
    user_choice = rock_paper_scissors_choices(choice)
#the above part of code calls in random function and generates a random choice out of 3 as AI's or computer's choice


    if user_choice == computer_output:
        print(f"Draw! You both played {choice}!")
        return choice
    won = False
#if statements displays diffrent outcomes of the draw
    
    if user_choice == "paper":
        if computer_output == "scissors":
            won = False
#if statements displays diffrent outcomes of the draw
            
        else:
            won = True
#if statements displays diffrent outcomes of the draw
            
    elif user_choice == "rock":
        if computer_output == "paper":
            won = False
#if statements displays diffrent outcomes of the draw
            
        else:
            won = True
#if statements displays diffrent outcomes of the draw
            
    elif user_choice == "scissors":
        if computer_output == "rock":
            won = False
#if statements displays diffrent outcomes of the draw
            
        else:
            won = True
#if statements displays diffrent outcomes of the draw

    if won:
        print("Congratulations,You conquer the victory by choosing",user_choice,"as the AI selected  ",computer_output)
#Print Statements runs if the user win and displays the moves
        
    else:
        print("Ohhh,That was a defeat and we made a wrong choice of",user_choice,"and the AI selected",computer_output)
#Print Statements runs if the user loses and displays the moves
        
    return user_choice
#return user choice  gives the user choice




def mario_exercise():
#The code line defines the mario exercise  

    victory_stairs = int(input("Enter the number of Stairs to Win"))
#the above code lines asks user for the number of Stairs to make Mario win

    for i in range(1, victory_stairs + 1):
#for statement if defined to print "# " as stairs


       print(" " * (victory_stairs - i) + "#" * i)
#Print Statements runs and prints the stairs

    print("Mario Won!\n But there are more levels until the queen ")
#aditional print statement to congratulate and warn at the same time


import time
#time function is called for delaying the run of code

def bye_exit():
#bye_exit code is defined to exit the module running
    
    print("Thank you For your Time Hope you like it!")
#finally thanking message for the user
    
    time.sleep(5)
#this code line delays the below function by 5 seconds

    exit()
#exit() kills the module and heads u back to code   
    


print("1. Modulo Calculator")
print("2. Integer Division Calculator")
print("3. For Loop Counter")
print("4. Float & Integer Calculator")
print("5. Print ASCII values of letters in a string")
print("6. Change Machine")
print("7. Rock Paper Scissors")
print("8. Mario wins a level")
print("00. For Exit")
#The above print statements appear in first and ask user to run their desired function



num = input("Please Enter the selection of number")
#this statement ask user to enter number code for their desired function


if num == "1":
    modulo_calc()
    
elif num == "2":
    int_division_Calc()
        
elif num == "3":
    for_loop_count()
        
elif num == "4":
    float_int_calc()
        
elif num == "5":
    ASCII_values_display()
        
elif num == "6":
    change_machine()
        
elif num == "7":
    rock_paper_scissors()
    
elif num == "8":
     mario_exercise()
        
elif num == "00":
    bye_exit()
#Above mentioned if ,elif statements run on the basis of user"s input and runs the function associated with number user enters.
    
else:
     print("Invalid input. Please enter a valid program number.")
#if the number code function is not available then it rejects the calling of any program and displays an error



#thank you the help and support sir
#this was the best i can perform 

    
