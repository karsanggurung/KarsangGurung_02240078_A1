import math
from pydoc import text


def is_prime(num):
    "check if a number is prime."
    if num <= 2:
        return False
    for i in range(2, num + 1):
        if num % i == 0:
            return False
        return True

def prime_sum(start, end):
    "calculate the sum of all prime numbers within a given range"
    sum=0
    for num in range(start,end+1):
        if is_prime(num):sum+=num
    return sum 

def length_converter(value, direction):
    "convert length from meters to feet"
    meters_to_feet = 3.28084
    feet_to_meters = 1/3.28084

    if direction == 'm':
        return round(value * meters_to_feet, 2)
    elif direction == 'f':
        return round(value * feet_to_meters, 2)
    else:
        return "Invalid direction!"
     

def consonant_counter(text):
    "Count the number of consonants in a given text string."
    consonants = "B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"
    count = 0
    for char in text:
        if char in consonants:
            count += 1
    return count


def min_max_finder(numbers):
    "find the smallest and larget number in a given list."
    if len(numbers) == 0:
        return "no numbers entered."
    return min(numbers),max(numbers)


def is_palindrome(text):
    "check if the given string is palindrome."
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    return cleaned_text == cleaned_text[::-1]
def word_counter(file_path):
    #   "counting occurance of specific words in a file"
    target_words = {"the": 0, "was": 0, "and": 0}
    try:
        with open(file_path,"r", encoding ='utf-8') as file:
            for line in file:
                words = line.split()
                
                for word in words:
                    cleaned_word = "".join(char.lower() for char in word if char.isalnum())  
                
                    if cleaned_word in target_words:
                        target_words[cleaned_word] += 1                  
    except FileNotFoundError:
        return "File not found."
    
    return target_words 


while True:
    print("menu")
    print("1. prime number sum")
    print("2. length unit converter")
    print("3. consonant counter")
    print("4. min_max finder")
    print("5. Palindrome checker")
    print("6. word counter")
    print("7. exit")
    
    choice = input("choose a function 1-7:")

    if choice == "1":
        start = int(input("enter start range:"))
        end = int(input("enter the end range:"))
        print(f"Total sum of the prime in given range is:{prime_sum(start, end)}")
        
    elif choice == "2":
        value = float(input(" enter the value:"))
        direction = input('Enter "m", for meters to feet or "f", for feet to meter:')
        print(f"Converted value:{length_converter(value, direction)}")


    elif choice == "3":
        text = input("enter the text:")
        print(f"The given consnant count:{consonant_counter(text)}")

    elif choice == "4":
         numbers = list(map(float, input("Enter numbers separated by space: ").split()))
         smallest, largest =  min_max_finder(numbers) 
         print(f"samllest: { min(numbers)}, largset: {max(numbers)}")
        

    elif choice == "5":
       text = input("enter your text:")
       print(f"palindrome {is_palindrome(text)}")

    elif choice == "6":
        file_path = input("enter file path:")
        print("number of words:", word_counter(file_path))
    
 
    elif choice == "7":
        print(F"exiting the menu")
        break
        
    else :
        print("unexpected error")
        break




        




            