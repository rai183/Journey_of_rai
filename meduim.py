import time # 👈 Import the time module
import os 

# Define the typewriter function
def typewriter_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05) # Adjust this value for faster or slower typing
    print() # Add a final newline after the entire message is printed

# --- Main Program Logic ---
print("\t\t\t===HELLO WELCOME TO THE EVAL FUNCTION OF PYTHON!===")

# 1. Input gathering
price = eval(input("Enter the price: "))
qtty = eval(input("Quantity: "))
os.system('cls')


# 2. Calculation
cost = price * qtty
discount = cost * 0.10
new_cost = cost - discount


# 3. Conditional output with typewriter effect
if cost >= 100:
    # Construct the message as a string
    message = f"\t\t\t===Here is the total with the 10% discount=== {new_cost}"
    # Use the typewriter function to display the message
    typewriter_print(message)
    
else:
    # Construct the message as a string
    message = f"\t\t\tHello, your total is not eligible for the discount, Here is the total: {cost}"
    # Use the typewriter function to display the message
    typewriter_print(message)