from rockpaperscissors2333.cli import play, simulate, stats, tutorial
from rockpaperscissors2333.game import reset_scoreboard
def main():
    while True:
        print("Welcome to Rock, Paper, Scissors!")
        print("1. Play against the computer")
        print("2. Simulate a game between two players")
        print("3. Reset the scoreboard")
        print("4. View game statistics")
        print("5. View tutorial")
        print("6. Quit")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            play()
        elif choice == "2":
            simulate()
        elif choice == "3":
            reset_scoreboard()
        elif choice == "4":
            stats()
        elif choice == "5":
            tutorial()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")    

if __name__ == "__main__":
    main()