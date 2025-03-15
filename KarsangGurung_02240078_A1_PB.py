
import random
#guess_number_game:
smallest = 1
largest = 10
    
# rock_paper_scissor_game:

option = ["Rock","Paper","Scissor"]

 
while True: 
        print("menu")
        print("1. guess_number_game.")
        print("2. rock_paper_scissor_game.")
        print("3. Exit program.")

        choice = input("choose a game 1-3:")

        if choice == "1":
            user_input = input("Enter (1-10): ").lower()
            
            comp = random.randint(smallest, largest)
            if user_input == comp:
                print("well done!")
                print("You win this round!")
            else:
                print("You lose this round!")
                continue
        elif choice == "2":
            
            user_choice = input("Enter rock, paper, or scissors:").lower()
            
            computer_choice = option[random.randint(0, 2)]            
            if user_choice == computer_choice:
                print("genius")
                print("You win this round!")
            else:
                print("You lose this round!")
            continue
    
         # Option 3: Quit the game

        elif choice == "3":
         print("Thanks for playing! Goodbye.")
        
        else:
            print("Invalid option. Please enter 1, 2, or 3.\n")
        break