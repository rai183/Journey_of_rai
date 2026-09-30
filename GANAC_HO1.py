def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
def compare_values(word_len, avg):
    if word_len > avg:

        print(f"The word length ({word_len}) is greater than the average ({avg:.2f}).")
    elif word_len < avg:
        print(f"The word length ({word_len}) is less than the average ({avg:.2f}).")
    else:
        print(f"The word length ({word_len}) is equal to the average ({avg:.2f}).")

def main():
    word = input("Enter a word: ")
    word_length = len(word)
    print(f"The word '{word}' has {word_length} characters.")
    num_list = []
    print(f"Please enter {word_length} number:")
    for i in range(word_length):
        while True:
            try:
                num = (input(f"Enter number {i + 1}: "))
                num_list.append(num)
                break
            except:
                print("Invalid input. Please enter a valid number.")

    avg = calculate_average(num_list)

    print("\n--- Results ---")
    print(f"List of numbers entered: {num_list}")
    print(f"Length of the word: {word_length}")
    print(f"Average of the numbers: {avg:.2f}")
    
    compare_values(word_length, avg)

if __name__ == "__main__":
    main()