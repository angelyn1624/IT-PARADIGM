import time



name = input("Enter your name: ")
yes_or_no = input("Do you want to start the program? yes/no: ")
if yes_or_no == "yes" or yes_or_no == "YES":
    
    print("--------------------------------------------------")
    print("HERE YOU GO!!", name,",WELCOME TO MY COMPILER:\n LOOK! :) :) ;) :O ")
    print("--------------------------------------------------")
   
while True:
    print("\n :) MENU LIST:\nTOPIC FOR THE 1ST SEMESTER")
    print("+=========================================+")
    print("!  A - Python language                    !")
    print("!  B - Python Escape Sequence             !")
    print("!  C - Print Statements                   !")
    print("!  D - Variables                          !")
    print("!  E - Operators                          !")
    print("!  F - Conditional Statements             !")
    print("!  G - Loop                               !")
    print("!  H - List                               !")
    print("!  I - Functions                          !")
    print("!  X - Exit                               !")
    print("+=========================================+")
    

    # Get input and convert it to uppercase to handle 'a' or 'A', 'x' or 'X'
    choice = input("Enter your choice:  ").upper()

    if choice == "A":
        
        # Your code will show here about the programming language python. 
        print("Please Wait.......")
        time.sleep(1)
        #This is the additional knowledge that i learned from exploring, in this code project.
        while True:
            print("+****************************+")
            print("*  Option 1 Submenu:         *")
            print("*  a - Definition            *")
            print("*  b - Example               *")
            print("*  c - Used for              *")
            print("*  d - Back to Main Menu     *")
            print("******************************")

            sub_choice = input("Enter your choice:  ")
            if sub_choice =='a':
                print("\n #Definition of python language:\n\n *Python is a high-level programming language that is easy to read and write.\nIt is used for creating applications,websites data analysis, and many other software tasks.\n")

                continue
            elif sub_choice == 'b':
                print("\n#Example of a Python language:\n\nPrint something - like hello world.\nAdd numbers: \nx = 7\ny = 4 \nand used print to run the program,\n print(x + y) and many more i will discuss in just a few minutes.\n ")
                # here in the programming language print statement is the number 1 used in coding because without this we can't run the program
                
                print("\nThe Output will be \nHello world!!")
                x = 7
                y = 4
                print(x + y)
                


                continue
            elif sub_choice == 'c':
                print("\nUsed For:\n - Web Development.\n - Mobile Apps.\n - Artificial Intelligence & Machine Learning\n - Cybersecurity.\n\tetc. \n")
                continue    
            
            elif sub_choice == 'd':
                print("\n Please Wait.......")
                time.sleep(1)

                break

            else:
                 print("\nChoice not recognized. Please enter a, b, c,  or d.")


       
        continue
        
   
    elif choice == "B":
        print("\nPlease Wait....")
        time.sleep(1)
        while True:
            print("+****************************+")
            print("*  Option 2 Submenu:         *")
            print("*  a - Definition            *")
            print("*  b - Example               *")
            print("*  c - Back to Main Menu     *")
            print("******************************")

            sub_choice = input("Enter your choice:  ")
            if sub_choice == 'a':
                print("\n#Definition of Python Escape Sequence:\n * In Python,an escape sequence is a special sequence of characters \nthat represents characters that are difficult \n or impossible to type directly, like newlines,tabs, or quotes\n")

                continue
            elif sub_choice == 'b':
                print("\n #Example of Python Escape Sequence:\n \n\u25CFThe newline sample- sandara is \nso beautiful.\n\u25CFthe single quote- yanni is \' cute.\n\u25CFBacklash sample- kiyoo is\\very good in playing basketball\n\u25CFTab- i am\t a quite person. \netc.\n ")
            #you can see in every sample, there is a different kind of sequence that use to phrase a word. the newline means that it creating a new line for the words, and in the backlash you can see in the word example that its also have a two slash between the sentence.The tab is for creating a space in your word you can see, if you run the program the sentence will have a gap.
            # in add i learn how to put a block dot for a list item slash \ u25cf.

                continue
            elif sub_choice == 'c':
                print("\nPlease Wait....")
                time.sleep(1)
                 
                break
            else:
                print("Choice not recognized. Please enter a, b, or c.")

                continue
    elif choice == "C":
        print("\nPlease Wait....")
        time.sleep(1)
        while True:
            print("+****************************+")
            print("*  Option 3 Submenu:         *")
            print("*  a - Definition            *")
            print("*  b - Example               *")
            print("*  c - Back to Main Menu     *")
            print("******************************")
            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("\n #Definition of Print Statement:\n*In Python, a print statement is also called now as a print function \nit show something in the output window like \n\n\u25CFtext\n\u25CFnumbers \n\u25CFresult of calculation or variable values.\n")

                continue
            elif sub_choice == 'b':
                print("\n #Example of Print Statement:\n \u25CFprint Hello World!\n\u25CFprint a number (5 + 3)\n \u25CFthe output will be 8.\nAlso a variable like\n \u25CFname = anna with double quotation because without the quotation the command will not process and\n it can cause a problem like error in the system \n")


                continue

            elif sub_choice == 'c':
                print("\nPlease Wait....")
                time.sleep(1)
                 
                break
            else:
                print("Choice not recognized. Please enter a, b, or c.")

                continue
                
    
    
    
        
    elif choice == "D":
        # Your code for Variable goes here
        print("Please wait...")
        time.sleep(1)
        while True:

            print("+****************************+")
            print("*  Option 4 Submenu:         *")
            print("*  a - Definition            *")
            print("*  b - Example               *")
            print("*  c -Thinks to Remember     *")
            print("*  d - Back to Main Menu     *")
            print("******************************")


            sub_choice=input("Enter Your Choice: ")
            if sub_choice == 'a':
                print("\n#Definition of Variables: \n *In Python, a variable in python is a storage name that holds data such as\n \u25CFnumber\n\u25CFtext\nor other values.\n")


                continue
            elif sub_choice == 'b':
                print("\n #Example of Variables: \n \n - Example Output for Variables: \n\u25CFName:tzusana \n\u25CFAge: 23\n\u25CFheight: 5.0")
                x = 'Tzusana' 
                y = 23 
                height = 5.0 
                print("Hi",x,"you're",y,"years old and your height is",height)
                print("\n #Example of Code: \n x = 'Tzusana' y = 23  Height = 5.0 \n print('Hi',x,'your',y,'years old and your height is',Height,')\n ") 


                continue
            elif sub_choice == 'c':
                print("\nThinks to remember:\n\u2022Must start with letter or\n\u2022cannot start with a number\n\u2022also no spaces,because its a case-sensitive.\n\u2022Should describe the value correctly \n")
                #because if you don't follow the rule there will be a conflict in running your program.
                continue
            
            elif sub_choice == 'd':
                print("\nPlease Wait....")
                time.sleep(1)
                 
                break
            else:
                print("Choice not recognized. Please enter a, b, c, or d.")

                continue
    elif choice == "E":
       print("\nPlease Wait....")
       time.sleep(1)
       while True:
            
            print("+****************************+")
            print("*  Option 5 Submenu:         *")
            print("*  a - Definition            *")
            print("*  b - Main Types of Operators")
            print("*  c - Example               *")
            print("*  d - Back to Main Menu     *")
            print("******************************")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                 print("\nOperators in Python are symbols or words used to perform operations \non values or variables like adding numbers, comparing values or checking condition.\n think of operators as a tool that let python calculate or compare things.\n")

                 continue
            elif sub_choice == 'b':
                print("\nMain Types of operators: \n 1.Arithmetic operators used for basic math operation.\n 2.Comparison Operators used to compare values.Result is True or False.\n 3.Logical Operators.Used for combining conditions \n 4.Assigntment Operators used to assigned values to variables.\n")

                continue
                
            elif sub_choice == 'c':
                print("\n*Examples of operators - \n Arithmetic \n\u25CF + Addition \n\u25CF - Subtraction \n\u25CF * Multiplication \n\u25CF / Division \n\u25CF % Modulus \n\u25CF** Exponent \n\u25CF // Floor Division ")
                print("\nComparison Operators \n\u25CF == Equal \n\u25CF != Not Equal \n\u25CF > Greater Than \n\u25CF < less than \n\u25CF >= Greater or equal \n\u25CF <= less or equal")
                print("\nLogical Operators \n\u25CF and - Both must be true - EX. 5  > 2 and 3 > 1 which is true \n\u25CF or - condition must be true . EX.5 > 9 or 4 > 1 which is true \n\u25CF not - reverses the result")
                print("\nAssignment Operators \n\u25CF = Assign value ex. x = 10 \n\u25CF += Add then assign ex. x += 5 \n\u25CF -= Subtract then assign ex. x -= 3 \n\u25CF *= Multiply then assign ex. x *= 2")
                print("\nExample:\n a = 5\n b = 3\n print(a > b and a == 5) The Output will be")
                a = 5
                b = 3 

                print(a > b and a == 5)
                #the output will be shown in the terminal


                continue
            elif sub_choice == 'd':
                print("\nPlease Wait....")
                time.sleep(1)
                 
                break
            else:
                print("\nChoice not recognized. Please enter a, b, c, or d.")
                continue


    elif choice == "F":
        print("\nPlease Wait....")
        time.sleep(1)
        while True:
            print("+********************************+")
            print("*  Option 6 Submenu:             *")
            print("*  a - Definition                *")
            print("*  b - Main Conditional Statement*")
            print("*  c - Example                   *")
            print("*  d - Importance                *")
            print("*  e - Back to Main Menu         *")
            print("**********************************")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("Definition:\n")
                print("\nIn Python, a condtional statement lets your program make decisions.\n It checks a condition (True or False), and runs a specific block of code\n depending on that result. \n ")

                continue

            elif sub_choice == 'b':
                print("Main conditional statement: \n\u2020 if statement - Run code only if the statement is true \n\u2020 if else statement - runs one block if true, another block if false. \n\u2022 if elif else statement - used when you have multiple conditions. \n")
                

                continue
            elif sub_choice == 'c':
                print(" Examples: \n\u2020 if statement - age = 23 if age >= 23: \n print('you are an adult') ")
                print("\nOutput\n")
                age = 23 

                if age >= 23:
                    print("you are an adult.")

                print("Example - if else statement \n\u2020 age = 16 \n if age >= 18: \n print('adult') \nelse: \n print('minor')\n ")
                print("\nOutput")
                age = 16 
                if age >= 18:
                    print("adult")
                else:
                    print("minor")
                
                print("\nif elif else statement -\n\u2020 grade = 85 \n if grade >= 90: \n print('excellent') \n elif grade >= 75: \n print('passed')\n else: \n\tprint('failed')\n" )
                print("\nOutput\n")
                grade = 85
                if grade >= 90:
                    print("excellent")
                elif grade >= 75:
                    print("passed")
                else:
                    print("failed")

               

                continue
            elif sub_choice == 'd':
                print("Importance : \n\u2020 Make decisions \n\u2020 Control the flow of the program \n\u2020 Run different actions based on user's input or data\n")
               
                continue

            elif sub_choice == 'e':
                print("\nPlease Wait....")
                time.sleep(1)
                 
                break

            else:
                print("\nChoice not recognized. Please enter a, b, c, d, or e.")
                continue
    

    elif choice == "G":
        print("\nPlease Wait....")
        time.sleep(1)
        while True:
            print("+********************************+")
            print("*  Option 7 Submenu:             *")
            print("*  a - Definition                *")
            print("*  b - Main Types of Loop        *")
            print("*  c - Example                   *")
            print("*  d - Used for                  *")
            print("*  e - Back to Main Menu         *")
            print("**********************************")

            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("Definition:\n")
                print("In Python, a Loop is a structure that lets your program repeat actions automatically.\n Instead of writing the same code many times, \na loop runs it again and again until a condition is met. \n ")

                continue

        
            elif sub_choice == 'b':
                print("Main Types of loop - \n\u25CF1. for loop - Used when you know how many times you want to repeat to repeat something.\n\u25CF 2. while loop you don't know exaactly how many times it will repeat, \n but it repeats as long as a condition is true \n ")

                continue

            elif sub_choice == 'c':
                print("\n\u25cf Examples - 1. for loop - print number 1 to 5, \n\u2020 for i in range(1,6): \n print(i) ")
                print("\n\u25cf Output\n")

                for i in range (1,11,1):
                    print(i)

                print("\n- Example of code\n")
                print("\u25cf loop through list - food = ['fries' , 'burger' , 'macaroni'] \nfor f in food: \n print(f)\n")
                print("\u25cfOutput\n")

                print("+++++++++++++++++++++++++++++++++")
                food = ["fries", "burger", "macaroni"]
                for f in food:
                    print(f)
                print("++++++++++++++++++++++++++++++++++")

                print("\t*", end = "")
            
                for a in range(1, 10, 1):
                    for b in range(9,a,-1):
                        print("", end=" ")
                    for c in range(1, a, 8):
                        print("*", end = " ")
                    for d in range(1, a, 1):
                        print("*", end= " ")   
                    print() 

                print("\n\u25cf Example: while loop ;")
                sum = 0
                for b in range(1,11,1):
                    print(b)
                    number = eval(input("Enter any number: "))
                    sum += number
                print("\n\t Output: \nThe sum of all the number is", sum)
                


            elif sub_choice == 'd':
                print("Used for: \n\u25CFloops help you avoid repeating code manually. \n\u25CF They are used when \n\u2022 printing repeated values \n\u2022processing items in a list \n\u2022 asking user input multiple times. \n\u2022 running a task until a condition stops.\n ")
 
            elif sub_choice == 'e':
                print("\nPlease Wait....")
                time.sleep(1)
                 
                break

            else:
                print("\nChoice not recognized. Please enter a, b, c, d, or e.")
                continue
    

    elif choice == "H":
        print("\nPlease Wait....")
        time.sleep(1)
        while True:
            print("+********************************+")
            print("*  Option 8 Submenu:             *")
            print("*  a - Definition                *")
            print("*  b - Example                   *")
            print("*  c - Feature of a list         *")
            print("*  d - Back to Main Menu         *")
            print("**********************************")
            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("\n Definition of a List - list is a collection of items stored in one variable\n it can hold many values at the same time, \n like number , words , or even mixed data.\n List are written with a square brackets []. \n")

                continue
    
            elif sub_choice == "b":
                print("\n Example: of a list think of it like a shopping list  ")
                print("\n Output\n")

                print("fruit = ['apple' , 'banana' , 'grapes']")

            elif sub_choice == "c":
                print("\n Feature of a list : \n\u2022 Can store multiple values \n\u2022 Can store different types of data \n\u2022 Item have indexes or position \n\u2022You can add, remove or change items \n")
                print("\n\u2022 Accesing Item Index - indexes start at 0 \n\u2022 you can see example below!.\n")
                print("fruit = ['apple' , 'banana' , 'grapes']\n")
                fruit = ["apple","banana","grapes"]
                print(fruit[0])
                print(fruit[1])
                print(fruit[2])

                print("\n\u2022 Changing Item - check the sample below !. \n")
                print("\n fruit[1] = 'peach' \n print(fruit) \n")

                fruit[1] = "peach"
                print(fruit)



                print("\n\u2022 Adding Items - check the sample below !. \n ")
                print("\nfruit.append('grapes')\n ")

                fruit.append("mango")


                print("Removing Items - check the sample below!. \n")
                print("\n fruit.remove('banana')\n ")

               

                print("\n List with mixed data - check the sample below!.\n")
                print("\n info = ['ange',23, 5.1,True]")

                info = ["ange", 23, 5.1, True]

                print("Another example : \n")



            
            elif sub_choice == 'd':
                print("\nPlease Wait....")
                time.sleep(1)
                 
                break

            else:
                print("\nChoice not recognized. Please enter a, b, c, or d.")
                continue
    
    elif choice == "I":
        print("\nPlease Wait....")
        time.sleep(1)
        while True:
            print("+****************************+")
            print("*  Option 9 Submenu:         *")
            print("*  a - Definition            *")
            print("*  b - Uses of function      *")
            print("*  c - Example               *")
            print("*  d - Back to Main Menu     *")
            print("******************************")
            sub_choice = input("Enter your choice: ")
            if sub_choice == 'a':
                print("\n #Definition of a Function :\n*In Python, a block of code that performs a specific task.\nYou can create and use it again and again than to create a new code ")

                continue
            elif sub_choice == 'b':
                print("Uses of function: \n\u2022 Avoid repeating code. \n\u2022 Make program organized. \n\u2022 Easier to read and fix. \n\u2022 Reusable.\n")

                continue
            elif sub_choice == 'c':
                print("This is the Example:\n def great ()\n print('hello world.')")
                print(" Use the keyword def to run the function")
                def greet ():
                    print("hello world.")
                print("This is another sample, function with parameter.\n")
                print("def say_you(name): \n print('heloo, ' + name)")
                def say_you(name):
                    print("heloo," + name)

            elif sub_choice == 'd':
                print("\nPlease Wait....")
                time.sleep(1)
                 
                break
            else:
                print("Choice not recognized. Please enter a, b, c, or d.")

                continue
            

            


    elif choice == "X":
        print("\n====================================")
        print(" YEY!! You did great ALL DONE! System Out. \n Thank you for Visiting my compiler program!\n See you Again!!.")
        print("====================================")
        break # This is the explicit stopping point
    else:
        print("Error Choice not recognized. Please select from the menu options (A-I, X).")
        continue # back to the main menu start of the loop and re-displays the menu