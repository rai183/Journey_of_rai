import os
# This is a simple Code Compiler Program using python.
# It shows information and runs an example based on user choices.

while True:  # Loop forever until the user chooses to exit
        # Clear the screen for a clean look (Windows only; use 'clear' on Mac/Linux)
       
        
        # Welcome message and menu
        print("\t\t\tWELCOME TO MY CODE COMPILER")
        print("\t\t\tGREETINGS USER! WHAT WOULD YOU LIKE TO DO?")
        print("\t\t\t-------------------------------------------------------")
        print("\t\t\tWHAT WHOULD YOU LIKE TO CHOOSE?")
        print("\t\t\t[1] - FUNCTIONS")
        print("\t\t\t[2] - ESCAPE SEQUENCES")
        print("\t\t\t[3] - LOOPS")
        print("\t\t\t[4] - CONDITIONAL STATEMENTS")
        print("\t\t\t[5] - LISTS")
        print("\t\t\t[6] - EXIT PROGRAM")


  # Get the user's choice
        choice = input("\n\t\t\tEnter your choice (1, 2, 3, 4, 5, 6): ")
        
        # Check what the user chose and call the right function
        if choice == "1":
                os.system('cls')
                print("1 - Print Function")
                print("2 - Input Function")
                print("3 - Def Function")
                print("4 - Eval Function")
                x = input("What would you like to choose?: ")
                if x == "1":
                        os.system('cls')
                        print("The print function allows the user to output information from the program to the user or developer.\n Hello World")
                        input("PRESS ENTER TO GO BACK TO MENU...")
                        os.system('cls')
                        continue
                elif x == "2":
                        os.system('cls')
                        print("The input function allows the user to input a data in the console and the program reads it")
                        input("What is your name?: ")
                        input("PRESS ENTER TO GO BACK TO MENU...")
                        os.system('cls')
                        continue
                elif x == "3":
                        os.system('cls')
                        print("It is the essential mechanism for creating a named, reusable block of code.")
                        input("PRESS ENTER TO GO BACK TO MENU...")
                        os.system('cls')
                        continue
                elif x == "4":
                        os.system('cls')
                        print("The eval function  Its primary purpose is to allow dynamic execution of code from strings, such as in calculators, configuration parsers, or interactive shells.")
                        something = eval(input("Input number --> "))
                        input("PRESS ENTER TO GO BACK TO MENU...")
                        os.system('cls')
                        continue

        
        
    
                
                

        elif choice == "6":
                print(("YOU HAVE EXITED THE PROGRAM", "\n THANK YOU!"))
                break