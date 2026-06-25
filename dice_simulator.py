import random

def roll_dice():
    print("Welcome to the Dice Roller Simulator!")
    
    while True:
        roll = input("Press 'Enter' to roll the dice, or 'q' to quit: ").lower()
        
        if roll == 'q':
            print("Thanks for playing! Goodbye.")
            break
            
        # Generating a random number between 1 and 6
        dice_value = random.randint(1, 6)
        print(f"🎲 You rolled a: {dice_value}\n")

if __name__ == "__main__":
    roll_dice()