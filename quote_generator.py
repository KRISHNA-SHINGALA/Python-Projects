import random
import time

def generate_quote():
    # List of quotes (you can easily add more here or fetch from an API later)
    quotes = [
        "Talk is cheap. Show me the code. - Linus Torvalds",
        "Programs must be written for people to read, and only incidentally for machines to execute. - Harold Abelson",
        "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler",
        "First, solve the problem. Then, write the code. - John Johnson",
        "Experience is the name everyone gives to their mistakes. - Oscar Wilde",
        "Code is like humor. When you have to explain it, it’s bad. - Cory House"
    ]
    
    print("\nFetching a brilliant quote for you...")
    time.sleep(1) # Adds a slight realistic delay
    
    print("-" * 50)
    print(random.choice(quotes))
    print("-" * 50)

if __name__ == "__main__":
    print("Welcome to the Daily Quote Generator!")
    while True:
        generate_quote()
        
        user_input = input("\nWould you like another quote? (y/n): ").lower()
        if user_input != 'y':
            print("Keep coding! See you next time.")
            break