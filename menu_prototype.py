
#BSIT - 1C ----- RAIZERE GANAC
#ITCS102 - FINAL PROJECT

import time
import os


def clear_sc():
    input("\n\nPRESS ENTER TO PROCEED TO THE NEXT PART...")
    os.system('cls')

def tap():
    
    Esc = input("\n\nPress Enter to show the Examples: ")
    if Esc == "":
        print("\n\n\t\t\t---Example Code---")
        print()

def Overview():

    print("")
    time.sleep(0.02)
    print ("\n\t\t\t\t----------OVERVIEW----------")
    time.sleep(0.02)
    text = ("\n\n\tIn 2023, studying programming is not just about coding; it's about equipping\n\tyourself with the skills and mindset to thirive in an increasingly digital and\n\tinterconnected world. Wheter you aspire to become a software engineer, a data\n\tscientist, an entrepreneur, or simply a tech-savvy individual, programming is a\n\tskill that empowers you to innovate, solve problems, and seize opportunities in\n\tthe digital landscape.\n")
    for char in text:
            print(char,end="",flush=True)
            time.sleep(0.01)
    clear_sc()
    
#-------------------INTRODUCTION---------------------------
def Introduction():

    isContinue = True
    while isContinue == True:
        time.sleep(0.3)
        print(f"\n\n\t\t\t----Python as a Programming Language----")

        print("\n\n\t\t\t\t\t_option_\n\n\t\t\ta\t---\tWhat is Python?\n\t\t\t\t---\tHistory of Python\n\t\t\tc\t---\tFeatures of Python\n\t\t\td\t---\tExit")
        
        time.sleep(1)
        Pili = input("\n\t\tChoose in the following: ")
        clear_sc()


        #What is Python
        if Pili.lower() == 'a':
            print ()
            print ("\t\t\t\t------What is Python?------")
            print ()

            text1 = ("\tPython is a dynamic, interpreted language without type declarations in its source code,\n\tmaking it concise and flexible. While it lacks compile-time type checking, it tracks\n\ttypes at runtime and raises errors when incompatible code is executed.\n\tPython is a versatile and beginner-friendly programming language widely used in fields\n\tlike data science and web development. Ranked among the top 10 'MOST POPULAR' and 'MOST LOVED'\n\ttechnologies, it empowers users to create almost anything.\n\n ")
            for char in text1:
                print(char,end="",flush=True)
                time.sleep(0.01)
            
            clear_sc()

        #History of Python
        elif Pili.lower() == 'b':
            print ()
            print ("\t\t\t\t-----History of Python-----")
            text2 = ("\n\n\tA Dutch-American computer programmer named Guido van Rossum created what is known as the Python\n\tprogramming language, first released in the early 1990s.\n\n\n\t● The development environment IDLE provided with Python comes from the name of a\n\t  member of the comic group.\n\n\t● Python has a simple syntax.\n\n\t● Python programs are clear and easy to read.\n\n\t● Python provides powerful programming features, and is widely used.\n\n\t● Companies and organizations that use Python include YouTube, Google, Yahoo, and NASA. Python is well\n\t  supported and freely available at www.python.org.\n\n")
            for char in text2:
                print(char,end="",flush=True)
                time.sleep(0.01)
            
            clear_sc()

        #Features of Python
        elif Pili.lower() == 'c':
            print()
            print("\t\t\t\t-----Features of Python------")
            
            text3 = ("\n\n\t\t● Object Oriented and Functional\n\t\t● Free\n\t\t● Portable \n\t\t● Powerful\n\t\t● Mixable\n\t\t● Easy to use\n\t\t● Easy to Learn\n\n")
            for char in text3:
                print(char,end="",flush=True)
                time.sleep(0.01)
            clear_sc()

        elif Pili.lower() == 'd':
            print("\n\t\t\t\t\t---Exit---")
            
            isContinue = False
        
        else:
            print ("\n\t\t\t\t= Invalid Input =\n")

def option1():
    time.sleep(0.5)
    print ("\n\n\t\tTypes of Comments in Python")
    print("\n\t\t\t\t\t_option_")
    print("\n\t\t\ta\t---\tSingle-line Comment\n\t\t\tb\t---\tMulti-line Comment\n\t\t\tc\t---\tExamples\n\t\t\td\t---\tExit")
            
def option2():
    print("\n\n\t\t\t1\t---\tExamples")
    print("\t\t\t2\t---\tExit")
    
#-------------------PRINT FUNCTION---------------------------
def print_F():
    
    import time
    isFunction = True

    while isFunction == True:
        print()
        print("\t\t\t\t----Print Statement----")
        print()
        print("\n\t\t\t\t\t_option_")
        print("\n\t\t\ta\t---\tComment")
        print("\t\t\tb\t---\tVariables")
        print("\t\t\tc\t---\tData Types")
        print("\t\t\td\t---\tUser Input")
        print("\t\t\te\t---\tExit")
        print()
        time.sleep(0.5)
        menu= input("Choose in the Following: ")
        clear_sc()

        if menu.lower() == 'a':
            print()
            print("\t\t\t\t----Comment----")
            print("")
            text4 = ("\tComments in Python are pieces of text that are ignored by the Python interpreter. They are\n\tused to Explain the code to reader, or to disable code that you don't want to run.") 
            for char in text4:
                print(char,end="",flush=True)
                time.sleep(0.01)
            
            #Type of Comments in Python
            option1()
            
            stay_menu1 = True
            while stay_menu1:
                comment = input("\n\nChoose in the Following: ")
                clear_sc()

                if comment.lower() == 'a':
                    print("\n\n\t\t\t-----Single-Line Comment------")
                    print("\t● Start with a hashtag symbol (#) and go to the end of the line.")
                    clear_sc()
                    option1()

                elif comment.lower() == 'b':
                    print("\n\n\t\t\t-----Multi-Line Comment------")
                    print('''\t● Start with three double quotes(""") and end with three double quotes''')
                    clear_sc()
                    option1()
                    
                elif comment.lower() == 'c':
                    print("\n\n\t\t\t-----Examples------")
                    print("\n\t---Single-Line Comments---")
                    print('''\t\t#This is a Single-Line Comment''')
                    print("\n\t---Multi-Line Comments---")
                    print('''\t\t"""
                    This is a multi-line cooment.
                    """ ''')
                    clear_sc()
                    option1()

                elif comment.lower() == 'd':
                    print("\n\t\t\t\t\t---Exit---")
                    stay_menu1 = False
                
                else:
                    print ("\n\t\t\t\t= Invalid Input =\n")
                    
                    option1()
                
        
        elif menu.lower() == 'b':
            print()
            stay_menu2 = True
            while stay_menu2:
                print("\t\t\t\t----Variables----")
                print("")
                text5 = ("\t● Variables in programming are like named boxes that can store information.\n\t You can use variables to store any type of data, such as numbers,\n\t strings, lists, and objects.") 
                for char in text5:
                    print(char,end="",flush=True)
                    time.sleep(0.01)

                option2()


                ask = input("\n\n\t\tChoose in the following: ")
                if ask == '1':
                    print("\n\n\t\t----Examples----")
                    print("\n\t\t my_name = John \n\t\t i = 20\n\t\t isContinue = True")
                    clear_sc()
                    
                elif ask == '2':
                    print("\n\t\t\t\t\t---Exit---")
                    clear_sc()
                    stay_menu2 = False
                    
                else:
                    print ("\n\t\t\t\t= Invalid Input =\n")
                    
            
        elif menu.lower() == 'c':
            print()
            stay_menu3 = True
            while stay_menu3:
                print("\t\t\t\t----Data types----")
                text6 = ("\n\n\tPython data types identify the type of data that a variable can store. ")
                for char in text6:
                    print(char,end="",flush=True)
                    time.sleep(0.01)
                print ("\n\tPython has the following data types built-in by default\n")
                print ("\t\t● Integers\t===\tint (123,1000)")
                print ('''\t\t● String\t===\tstr ("Hello",'Word', "2005")''')
                print ("\t\t● Float\t\t===\tfloat (1.50,2005.20)")
                print ("\t\t● Boolean\t===\tbool (True,False)")
                
                    #===Examples===
                ask_ex = input("\n\n\t\tPress Enter to show the Examples [x] to exit: ")

                if ask_ex == "":
                    print("\n\n---Example Code---")

                    print("\n\n\t==INPUT==")
                    print('''\n\tage = 20 # ---Integer''')
                    print('''\n\tprice = 19.99  # ---Float''')
                    print('''\n\tname = "Marcus"  # ---String''')
                    print('''\n\tisStudent = True  # ---Float\n\n''')

                    print('''\tprint("Age: ", age) ''')
                    print('''\tprint("Price: ", price)''')
                    print('''\tprint("Name: ",name)''')
                    print('''\tprint("Is Student: ", isStudent)''')

                    print("\n\n\t==OUTPUT==")
                    print('''\n\tAge: 20 ''')
                    print('''\n\tPrice: 19.99 ''')
                    print('''\n\tName:Marcu;s  ''')
                    print('''\n\tIs Student: True \n\n''')
                    clear_sc()

                elif ask_ex.lower()== 'x':
                    print("\n\t\t\t===Exit===")
                    clear_sc()
                    stay_menu3 = False

                else:
                    print("==Just Press Enter key on your Keyboard==")
            
        elif menu.lower() == 'd':
            print()
            stay_menu4 = True
            while stay_menu4:
                print("\t\t\t\t----User Input----")
                text7 = ('''\n\n\tPython provides the input() function.input() reads what 
            the user types on the keyboard and return it as a string \n\n''')
                for char in text7:
                    print(char,end="",flush=True)
                    time.sleep(0.01)
                ask_ex3 = input("\n\n\t\tPress Enter to show the Examples [x] to exit: ")

                if ask_ex3 == "":
                    print("\n\n\t\t---Example Code---")
                    print()
                    name = input("\tEnter your name: ")

                    print("\n\tHi, ",name," Welcome to my program!")
                    print("\n\n\t===================Code===========================")
                    time.sleep(1)
                    print("\n\t==INPUT==")

                    print('''\t name = input("Enter your name: ")
                    print("Hi,",name," Welcome to my program!) ''')
                    time.sleep(1)
                    print("\n\n\t==OUTPUT==")
                    print('''Hi,(your input) Welcome to my program!''' )
                    clear_sc()
            
                elif ask_ex3.lower()== 'x':
                    print("\n\t\t\t===Exit===")
                    clear_sc()
                    stay_menu4 = False
                else: 
                    print ("\n\t\t\t\t= Invalid Input =\n")
        
        elif menu.lower() == 'e':
            print ("\n\t\t\t\t= Exit =\n")
            isFunction = False

        else:
            print ("\n\t\t\t\t= Invalid Input =\n")

#-------------------OPERATORS---------------------------
def operator():
    isCorrect = True
    while isCorrect == True:
        time.sleep(0.3)
        print(f"\n\n\t\t\t----Python Operators----")
        print("\n\n\t\t\t\t_option_\n\n\t\t\ta\t---\tDefinition\n\t\t\tb\t---\tTypes\n\t\t\tc\t---\tExit")
        time.sleep(1)
        operator = input("\n\t\tChoose in the following: ")

        if operator.lower() == 'a':
            print("\n\n\t\t\t\t----Python Operators----")
            print("")
            text8 = ('''\n\tOperators are used to perform operations on variables and values.
         ''')
            for char in text8:
                print(char,end="",flush=True)
                time.sleep(0.01)
            clear_sc()

        
        elif operator.lower() == 'b':
            text9 = ('''\n\tPython divides the operators in the following groups:''')
            for char in text9:
                print(char,end="",flush=True)
                time.sleep(0.01)

           
            
            stay_menu5 = True
            while stay_menu5: 
                time.sleep(0.5)
                print("\n\n\t\t\t===Option===")
                print('''\n\t\t    a\t---\tArithmetic operators
                    b\t---\tAssignment operators
                    c\t---\tComparison operators
                    d\t---\tLogical operators
                    e\t---\tExit
                        ''') 
                ask_Opera = input("\n\t\tChoose in the following: ")
                clear_sc()

                if ask_Opera.lower() == 'a':

                    print ("\n\t\t\t==Arithmetic Operators==") 

                    text10 = ('''\n\tArithmetic operators are used with numeric values to perform common 
                            mathematical operations:
                    
                \tOperator\tName\n\n\t\t\t+\t\tAddition\n\t\t\t-\t\tSubtraction\n\t\t\t*\t\tMultiplication\n\t\t\t/\t\tDivision\n\t\t\t%\t\tModulus\n\t\t\t**\t\tExponentiation\n\t\t\t//\t\tFloor Division ''')
                    for char in text10:
                        print(char,end="",flush=True)
                        time.sleep(0.01)
                    
                    print()
                    tap()
                    num = eval(input("\t\tEnter a number --> "))
                    numb = eval(input("\t\tEnter second number --> "))

                    sum = num + numb

                    print("\t\tthe sum of ", num, "+",numb," = ",sum)

                    print("\n\n\t\t\t==INPUT==")
                    print('''\n\n\tnum = eval(input("Enter a number --> "))
            numb = eval(input("Enter second number --> "))

            sum = num + numb

            print("the sum of ", num, "+",numb," = ",sum)
    ''')
                    clear_sc()



                elif ask_Opera.lower() == 'b':
                    print ("\n\t\t\t==Assignment Operators==")
                    text11 = ('''\n\tAssignment operators are used to assign values to variables:
                                =
                                +=
                                -=
                                *=
                                /=
                                %=
                                //=
                                **=  ''')
                    for char in text11:
                        print(char,end="",flush=True)
                        time.sleep(0.01)
                    print()
                    tap()
                    time.sleep(0.5)
                    x = 5

                    print ("\t",x)

                    x+=5
                    print ("\t",x)

                    x += 10
                    print ("\t",x)

                    x += 15
                    print ("\t",x)

                    x +=20
                    print ("\t",x)

                    x += 25
                    print ("\t",x)
                    
                    time.sleep(0.5)
                    print("\n\n\t\t\t==INPUT==")
                    print('''\n\n\tx = 5

            print (x)

            x+=5
            print (x)

            x += 10
            print (x)

            x += 15
            print (x)

            x +=20
            print (x)

            x += 25
            print (x)
    ''')
                    time.sleep(0.5)
                    clear_sc()

                
                elif ask_Opera.lower() == 'c':
                    3
                    print ("\n\t\t\t==Comparison operators==")
                    text12 = ('''\n\tComparison operators are used to compare two values:
                            
                        Operator\tName
                            ==\t\tEqual
                            !=\t\tNot Equal
                            >\t\tGreater Than
                            <\t\tLess Than
                            >=\t\tGreater Than or Equal to
                            <=\t\tLess Than or Equal to
                                ''')
                    for char in text12:
                        print(char,end="",flush=True)
                        time.sleep(0.01)
                    print()
                    tap()
                    print()
                    time.sleep(0.5)
                    Age = eval(input("\n\t\tEnter your age ---> "))

                    #1-7 - Toddler
                    #8-13 - pre teen
                    #14-18 - teenager
                    #19-31 - early adulthood
                    #32-45 - Mid adulthood
                    #46-59 - post adulthood
                    #60 + - senior

                    if Age <= 7:
                        print("\t\tYour age is categorized as toddler")

                    elif Age <= 13 and Age >= 8:
                        print ("\t\tYour age is categorized as Pre teen")

                    elif Age <=18 and Age >=14:
                        print ("\t\tYour age is categorized as Teenager")

                    elif Age <=31 and Age >= 19:
                        print ("\t\tYour age is categorized as Early Adulthood")

                    elif Age <=45 and Age >= 32: 
                        print ("\t\tYour age is categorized as Mid Adulthood")

                    elif Age <= 59 and Age >= 46:
                        print ("\t\tYour age is categorized as Post Adulthood")

                    elif Age >= 60:
                        print ("\t\tYour age is categorized as Senior")

                    time.sleep(0.5)
                    print("\n\n\t\t\t==INPUT==")
                    print('''\n\n\tAge = eval(input(" Enter your age ---> "))

                    #1-7 - Toddler
                    #8-13 - pre teen
                    #14-18 - teenager
                    #19-31 - early adulthood
                    #32-45 - Mid adulthood
                    #46-59 - post adulthood
                    #60 + - senior

                    if Age <= 7:
                        print("Your age is categorized as toddler")

                    elif Age <= 13 and Age >= 8:
                        print ("Your age is categorized as Pre teen")

                    elif Age <=18 and Age >=14:
                        print ("Your age is categorized as Teenager")

                    elif Age <=31 and Age >= 19:
                        print ("Your age is categorized as Early Adulthood")

                    elif Age <=45 and Age >= 32: 
                        print ("Your age is categorized as Mid Adulthood")

                    elif Age <= 59 and Age >= 46:
                        print ("Your age is categorized as Post Adulthood")

                    elif Age >= 60:
                        print ("Your age is categorized as Senior")
    ''')
                    
                    print("\n\n\t===Exit===")
                    clear_sc()

                elif ask_Opera.lower() == 'd':
                    print ("\n\t\t\t\tLogical Operators\n")
                    text12 = ('''\n\tLogical operators are used to combine conditional statements:
                                ==\tEqual
                                !=\tNot Equal
                                >\tGreater Than
                                <\tLess Than
                                >=\tGreater Than or Equal to
                                <=\tLess Than or Equal to
                                ''')
                    for char in text12:
                        print(char,end="",flush=True)
                        time.sleep(0.01)
                    print()
                    tap()
                    print()
                    gold = 0

                    miner = input("\n\n\tHi, What is your name: ")

                    isGold = input ("\tis the mineral gold? ")

                    if isGold.lower() == "yes":
                        gold += 1
                        print (f"\n\tHi {miner}, Your total number of gold is {gold}")
                    else:
                        print (f"\n\tHi {miner}, Your total number of gold is {gold}") 
                    
                    time.sleep(0.5)
                    print("\n\n\t\t\t==INPUT==")
                    print('''\n\n\tgold = 0

                    miner = input("\n\n\tHi, What is your name: ")

                    isGold = input ("\tis the mineral gold? ")

                    if isGold.lower() == "yes":
                        gold += 1
                        print (f"\n\tHi {miner}, Your total number of gold is {gold}")
                    else:
                        print (f"\n\tHi {miner}, Your total number of gold is {gold}") 
                    
    ''')
                    clear_sc()

                
                elif ask_Opera.lower() == 'e':
                    print ("\n\t\t\t\t= Exit =\n")
                    
                    stay_menu5 = False



        elif operator.lower() == 'c':
            print ("\n\t\t\t\t= Exit =\n")
            clear_sc()
            isCorrect = False
        
        else:
            print ("\n\t\t\t\t= Invalid Input =\n")

            continue


def conditional_St():
    isTama = True
    while isTama == True:
        time.sleep(0.3)
        print(f"\n\n\t\t\t----Conditional Statements----")

        print("\n\n\t\t\t\t_option_\n\n\t\t\ta\t---\tDefinition\n\t\t\tb\t---\tNested Condition\n\t\t\tc\t---\tExit")
        
        time.sleep(1)
        con_Sta = input("\n\t\tChoose in the following: ")

        if con_Sta.lower() == 'a':
            print("\n\n\t\t\t\t----Conditional Statements----")
            print("")
            text13 = ('''\n\tConditional statements (if, else, and elif) are fundamental programming 
        constructs that allow you to controlthe flow of your program based on conditions 
        that you specify. They provide away to make decisions in your program and execute 
        different code based on those decisions.
        ''')
            for char in text13:
                print(char,end="",flush=True)
                time.sleep(0.01)

            print()
            tap()
            name = input("\tEnter your name ---> ")
            password = input("\tEnter your password (helloworld , kaya_ko) ---> ")

            if password.lower() == "helloworld":
                print ("\tAccess Granted")
                print (f"\tHi,{name} I hope You enjoy the system")

            elif password.lower() == "kaya_ko":
                print ("\tAccess Granted")
                print (f"\tHi,{name} I hope You enjoy the system")

            else :
                print ("\n\n\t\t==Access Denied==")

            print("\n\n\tsystem exit")
            
            print("\n\n\t\t\t==INPUT==")
            print('''\n\n\tname = input("Enter your name ---> ")
                password = input("Enter your password (helloworld , kaya_ko) ---> ")

                if password.lower() == "helloworld":
                    print ("Access Granted")
                    print (f"Hi,{name} I hope You enjoy the system")

                elif password.lower() == "kaya_ko":
                    print ("Access Granted")
                    print (f"Hi,{name} I hope You enjoy the system")

                else :
                    print ("Access Denied")

                print("system exit")
            
''')
            clear_sc()



        
        elif con_Sta.lower() == 'b':
            print("\n\n\t\t\t\t----Nested Condition----")
            print("")
            text14 = ('''\n\tThe nested if statements in Python are the nesting of an if
        statement inside another if statement with or without an else statement.
        ''')
            for char in text14:
                print(char,end="",flush=True)
                time.sleep(0.01)

            print()
            tap()
           # Grocery

            print ("\n\n  ------------------GROCERY------------------")
            name = input ("\n\n\tPlease Enter your name: ")

            grocery = input("\tDid you buy a grocery(Yes/No) ---> ")

            if grocery.lower() == "yes":
                item = input("\n\tName  of the item: ")
                price = eval(input("\tPrice of the item: "))
                Age = eval(input("\tEnter your age: "))
                
                if Age < 60:
                    tax = price * .12
                    Nprice = tax + price
                
                    print(f"\n\n\tHi {name}, your purchased a {item}, with a price of {price} PHP plus 12% tax ({round(tax,2)}), total of \033[4m{round(Nprice,2)} PHP\033[0m")
                    
                    amount = eval(input("\n\tAmount given : "))
                    change =  amount - Nprice
                    print(f"\n\tChange : \033[4m{round(change,2)} PHP\033[0m") 

                    print ("\n\n\t     Thank you for using the System")
                    
                elif Age >= 60:
                    tax = price * .12
                    Nprice = tax + price

                    discount = Nprice * 0.052
                    Dprice = Nprice - discount
                    print (f"\n\n\tHi {name}, your purchased a {item}, with a price of {price} PHP plus 12% tax ({round(tax,2)}),  total of {Nprice} PHP,")
                    print (f"\tBut you will get a senior discount at 5.2% ({round(discount,2)}), total of \033[4m{round(Dprice,2)} PHP\033[0m")

                    
                    amount = eval(input("\n\tAmount given : "))
                    change =  amount - Dprice
                    print(f"\n\tChange : \033[4m{round(change,2)} PHP\033[0m") 

                    print ("\n\n\t     Thank you for using the System")


            else :
                print ("\n\n\t  .........No Grocery Purchased.........")

            print ("\n\n\t\t----- System Exit -----")

            time.sleep(1)
            print("\n\n\t\t\t==INPUT==")
            print('''\n\n\t# Grocery

            print ("\n\n  ------------------GROCERY------------------")
            name = input ("\n\n\tPlease Enter your name: ")

            grocery = input("\tDid you buy a grocery(Yes/No) ---> ")

            if grocery.lower() == "yes":
                item = input("\n\tName  of the item: ")
                price = eval(input("\tPrice of the item: "))
                Age = eval(input("\tEnter your age: "))
                
                if Age < 60:
                    tax = price * .12
                    Nprice = tax + price
                
                    print(f\n\n\tHi {name}, your purchased a {item}, with a price of {price} PHP plus 12% tax ({round(tax,2)}), total of \033[4m{round(Nprice,2)} PHP\033[0m")
                    
                    amount = eval(input("\n\tAmount given : "))
                    change =  amount - Nprice
                    print(f"\n\tChange : \033[4m{round(change,2)} PHP\033[0m") 

                    print ("\n\n\t     Thank you for using the System")
                    
                elif Age >= 60:
                    tax = price * .12
                    Nprice = tax + price

                    discount = Nprice * 0.052
                    Dprice = Nprice - discount
                    print (f"\n\n\tHi {name}, your purchased a {item}, with a price of {price} PHP plus 12% tax ({round(tax,2)}),  total of {Nprice} PHP,")
                    print (f"\tBut you will get a senior discount at 5.2% ({round(discount,2)}), total of \033[4m{round(Dprice,2)} PHP\033[0m")

                    
                    amount = eval(input("\n\tAmount given : "))
                    change =  amount - Dprice
                    print(f"\n\tChange : \033[4m{round(change,2)} PHP\033[0m") 

                    print ("\n\n\t     Thank you for using the System")


            else :
                print ("\n\n\t  .........No Grocery Purchased.........")

            print ("\n\n\t\t----- System Exit -----\n\n")''')


            clear_sc()


        elif con_Sta.lower() == 'c':
                print ("\n\t\t\t\t= Exit =\n")
                clear_sc()

                break
            
        else:
            print ("\n\t\t\t\t= Invalid Input =\n")

            continue


def Looping():
    isLoop = True
    while isLoop == True:
        time.sleep(0.3)
        print(f"\n\n\t\t\t----Loops----")

        print("\n\n\t\t\t\t_option_\n\n\t\t\ta\t---\tDefinition\n\t\t\tb\t---\tTypes\n\t\t\tc\t---\tExit")
        
        time.sleep(1)
        Lo_op = input("\n\t\tChoose in the following: ")

        if Lo_op.lower() == 'a':
            print("\n\n\t\t\t\t----Python Loops----")
            print("")
            text15 = ('''\n\tA loop is an instruction that repeats multiple times as long as some 
                      condition is met.
        ''')
            for char in text15:
                print(char,end="",flush=True)
                time.sleep(0.01)
            print()
            clear_sc()

        elif Lo_op.lower() == 'b':
            stay_menu6 = True
            while stay_menu6:
                print("\n\n\t\t\t\t----Types of Loops----")
                print("")
                text16 = ('''\n\tPython has two primitive loop commands:

                a\t---\twhile loops
                b\t---\tfor loops
                c\t---\tExit
            ''')
                for char in text16:
                    print(char,end="",flush=True)
                    time.sleep(0.01)
                print()
                Lo_op_inpt = input("\n\t\tChoose in the following: ")
                clear_sc()

                if Lo_op_inpt.lower() == 'a':

                    print("\n\n\t\t\t\t----While Loops----")
                    print("")
                    text17 = ('''\n\tThe while loop we can execute a set of statements as long as a condition is true.
                ''')
                    for char in text17:
                        print(char,end="",flush=True)
                        time.sleep(0.01)
                    print()

                

                    print()
                    tap()
                # example

                    print ("\n\n  ------------------While Loops------------------")
                    print ()
                    tuloy = True
                    num = 0
                    
                    while tuloy == True:
                        name = input ("\tEnter a name(Enter 'stop' to Terminate the Program) --> ")
                        if name.lower() == "stop":
                            print()
                            print ("\t--Loop Terminated--")
                            print ()
                            print ("\tYou have total of ",num," names entered ")
                            print ()
                            break
                            tuloy = False
                        
                        else:
                            num += 1
                            continue

                    time.sleep(1)
                    print("\n\n\t\t\t==INPUT==")
                    print('''\n\n\ttuloy = True
                    num = 0
                    
                    while tuloy == True:
                        name = input ("Enter a name(Enter 'stop' to Terminate the Program) --> ")
                        if name.lower() == "stop":
                            print()
                            print ("--Loop Terminated--")
                            print ()
                            print ("You have total of ",num," names entered")
                            print ()
                            break
                            tuloy = False
                        
                        else:
                            num += 1
                            continue
        ''')


                    clear_sc()


                elif Lo_op_inpt.lower() == 'b':
                    print("\n\n\t\t\t\t----For Loops----")
                    print("")
                    text18 = ('''\n\tA for loop is used for iterating over a sequence (that is either a list, 
            a tuple, a dictionary, a set, or a string).
                            
        This is less like the for keyword in other programming languages, and works more 
        like an iterator method as found in other object-orientated programming languages.
        With the for loop we can execute a set of statements
                ''')
                    for char in text18:
                        print(char,end="",flush=True)
                        time.sleep(0.01)
                    print()

                    print()
                    tap()
                # example
                    print ("\n\n  ------------------For Loops------------------")
                    print()

                    for x in range (8,1,-1):

                        for z in range (x,0,-1):
                            print (" ", end=" ")
                        
                        for y in range ( 7, x, -1):
                            print("*", end = " ")

                        for a in range (7,x,-1):
                            print ("*", end = " ")
                        print()


                    for x in range (5,0,-1):

                        for z in range (6,0,-1):
                            print (" ", end=" ")
                        
                        for y in range (1,2):
                            print("*", end = " ")

                        for a in range (1,2):
                            print ("*", end = " ")
                        print()

                    print ()

                    time.sleep(1)
                    print("\n\n\t\t\t==INPUT==")
                    print('''\n\n\tfor x in range (8,1,-1):

                        for z in range (x,0,-1):
                            print (" ", end=" ")
                        
                        for y in range ( 7, x, -1):
                            print("*", end = " ")

                        for a in range (7,x,-1):
                            print ("*", end = " ")
                        print()


                    for x in range (5,0,-1):

                        for z in range (6,0,-1):
                            print (" ", end=" ")
                        
                        for y in range (1,2):
                            print("*", end = " ")

                        for a in range (1,2):
                            print ("*", end = " ")
                        print()
    ''')
                    
                    clear_sc()

                elif Lo_op_inpt.lower() == 'c':
                    print ("\n\t\t\t\t= Exit =")
                    clear_sc()

                    stay_menu6 = False
                
                else:
                    print ("\n\t\t\t\t= Invalid Input =\n")
                    continue

        elif Lo_op.lower() == 'c':
                print ("\n\t\t\t\t= Exit =\n")
                clear_sc()

                break
            
        else:
            print ("\n\t\t\t\t= Invalid Input =\n")
            continue



def List():
    isList = True
    while isList == True:
        time.sleep(0.3)
        print(f"\n\n\t\t\t----List----")

        print("\n\n\t\t\t\t_option_\n\n\t\t\ta\t---\tDefinition & Example\n\t\t\tb\t---\tExit")
        
        time.sleep(1)
        Li_st = input("\n\t\tChoose in the following: ")
        clear_sc()

        if Li_st.lower() == 'a':
            print("\n\t\t\t\t----Lists----")
            text19 = ('''\n\tLists are used to store multiple items in a single variable.
        ''')
            for char in text19:
                print(char,end="",flush=True)
                time.sleep(0.01)
            print()
            print()
            tap()
            # example
            print ("\n\n  ------------------List------------------")
            print()
            myName1 = ['Raizere','Angelo', 'Ganac']

            print (myName1)

            time.sleep(1)
            print("\n\t\t\t==INPUT==")
            print('''\n\tmyName1 = ['Raizere','Angelo', 'Ganac']

            print (myName1)
''')
            clear_sc()

        elif Li_st.lower() == 'b':
                clear_sc()

                break
            
        else:
            print ("\n\t\t\t\t= Invalid Input =\n")

            continue
    
def func_tion():
    isFunc = True
    while isFunc == True:
        time.sleep(0.3)
        print(f"\n\n\t\t\t----Function----")

        print("\n\n\t\t\t\t_option_\n\n\t\t\ta\t---\tDefinition & Example\n\t\t\tb\t---\tExit")
        
        time.sleep(1)
        Fun_tion = input("\n\t\tChoose in the following: ")

        if Fun_tion.lower() == 'a':
            print("\n\n\t\t\t\t----Function----")
            text21 = ('''\n\tA function is a block of code which only runs when it is called.''')
            for char in text21:
                print(char,end="",flush=True)
                time.sleep(0.01)
            print()
            print()
            tap()
            # example
            print ("\n\n  ------------------Function------------------")
            print()
            def na_me():
                your_Name =input("Enter your name: ")

                print ("Hello!, ",your_Name)

            na_me()

            time.sleep(1)
            print("\n\t\t\t==INPUT==")
            print('''\n\n\tdef na_me():
                your_Name =input("Enter your name: ")

                print ("Hello!, ",your_Name)

                na_me()
''')
            clear_sc()
        
        elif Fun_tion.lower() == 'b':
                clear_sc()

                break
            
        else:
            print ("\n\t\t\t\t= Invalid Input =\n")

            continue
    


            

def menu():
    print("")
    text20 = ('''\t\t\t====Welcome to this simple guide on Python programming!====
          
          In this journey, we'll learn the basics of Python, like variables, print statements, 
          functions, and more. Let's start exploring Python step by step. Get ready for an 
          exciting adventure into coding!''')
    for char in text20:
        print(char,end="",flush=True)
        time.sleep(0.01)
    
    time.sleep(1)

def Me_nu():
    print('''\n\n\t\t\t===Main Menu===

        [1] - Introduction 
        [2] - Print Statements
        [3] - Operators
        [4] - Conditionals
        [5] - Loops
        [6] - Functions
        [7] - Lists
        [8] - Exit'''
    )
    print ()

     
menu()
while True:
    Me_nu()

    main_menu = input("Enter your choice here: ")

    if main_menu == '1':
        clear_sc()
        Overview()
        Introduction()
        

    elif main_menu == '2':
        clear_sc()
        print_F()
        
    elif main_menu == '3':
        clear_sc()
        operator()
        

    elif main_menu == '4':
        clear_sc()
        conditional_St()
        

    elif main_menu == '5':
        clear_sc()
        Looping()
        

    elif main_menu == '6':
        clear_sc()
        func_tion()
        
        

    elif main_menu == '7':
        clear_sc()
        List()
        
        

    elif main_menu == '8':
        print("\n\t\t\t===Menu Terminated===")
        clear_sc()
        break
    
    else:
        print("\n\t\t==invalid input==")
        clear_sc()
        continue
