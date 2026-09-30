num_list = []

word = input("Enter a word: ")

for i in range(len(word)):
    numbers = int(input(f"Enter number {i+1}:"))
    num_list.append(numbers)

def avg(num_list):
    total = sum(num_list)
    avg = total / len(word)
    return avg

def check(num_list, word, avg,):
    print(num_list)
    print(f'The lenght of the word is {len(word)}.')
    print(f'The average of the number is {avg}.')

    if len(word) > avg:
        print(f'The lenght of the word {word} is greater than the average')
    elif len(word < avg):
        print(f'The lenght of the word {word} is less than the average')
