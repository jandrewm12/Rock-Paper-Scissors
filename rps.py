#This program is a Rock, Paper, Scissors game!
import random
import pickle

game_round = 0
wlt = 0
comp_choice = 0
player_choice = 0
rps = 0
comp_rps = ""
user_name = ""
win_counter = 0
lose_counter = 0
tie_counter = 0
rps_file = 0
choice = 0
other_choice = 0
ratio = 0
end = 0
stats = []

#computer randomly chooses rps
def computer_choice():
    global comp_rps
    global comp_choice
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_rps = "Rock"
    elif comp_choice == 2:
        comp_rps = "Paper"
    elif comp_choice == 3:
        comp_rps = "Scissors"

#user chooses rps
def user_choice():
    global rps
    global choice
    while(True):
        try:
            player_choice = input("What will it be? ")
            try:
                choice = int(player_choice)
            except:
                "Please enter a number."
                continue

            if choice == 1:
                rps = "Rock"
                return choice
                
            elif choice == 2:
                rps = "Paper"
                break
            elif choice == 3:
                rps = "Scissors"
                break
            else:
                print("Please enter 1, 2, or 3.")
                continue
            return int(player_choice)

        except:
            "Please enter a number."
            continue

#calculates results of the match
def game_results():
    results = ""
    global tie_counter
    global lose_counter
    global win_counter
    global wlt


    #user's choice is compared to computer's
    if choice == comp_choice:
        wlt = 3
        tie_counter += 1
    elif choice == 1 and comp_choice == 2:
        wlt = 2
        lose_counter += 1
    elif choice == 1 and comp_choice == 3:
        wlt = 1
        win_counter += 1
    elif choice == 2 and comp_choice == 1:
        wlt = 1
        win_counter += 1
    elif choice == 2 and comp_choice == 3:
        wlt = 2
        lose_counter += 1
    elif choice == 3 and comp_choice == 2:
        wlt = 1
        win_counter += 1
    elif choice == 3 and comp_choice == 1:
        wlt = 2
        lose_counter += 1

    #wlt is converted to win, lose, tie
    if wlt == 1:
        results = "win!"
    elif wlt == 2: 
        results = "lose."
    elif wlt == 3:
        results = "tie."

    print("You chose " + rps + ". The computer chose " + comp_rps + ". You " + results)

#loads a previous game
def load_game():
    global rps_file
    global stats
    global win_counter
    global lose_counter
    global tie_counter
    while(True):
        try:
            file_name = str(user_name + ".rps")
            rps_file = open(file_name, "rb")

            #write previous game stats to statistics
            statistics = pickle.load(rps_file)
            stats = statistics

            win_counter = stats[1]
            lose_counter = stats[2]
            tie_counter = stats[3]
            rps_file.close()

            rps_file = open(file_name, "wb")

            
            print("Welcome back, " + user_name + ". Let's play!")
            print("")
            game()
            break
        except:
            print(user_name, ", your game could not be found.")
            break


#rps gameplay
def game():
    while(True):
        try:
            global game_round 
            global other_choice 
            global user_name 
            global win_counter
            global lose_counter
            global tie_counter
            global ratio
            global end
            game_round += 1
            if end == 1:
                break
            
            print("Round " + str(game_round))
            print("")

            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("")
            
            user_choice()
            print("")
            computer_choice()
            print("")
            game_results()
            print("")
            after_game_menu()
            print("")
        except:
            print("An error has occurred in game()")

#this menu occurs after a game is played
def after_game_menu():
    global other_choice 
    global user_name 
    global win_counter
    global lose_counter
    global tie_counter
    global ratio
    global end
    global stats
    global rps_file
    while(True):
        try:
            if end == 1:
                break

            print("What would you like to do? ")
            print("")
            print("1. Play again")
            print("2. View statistics")
            print("3. Quit")
            print("")

            other_choice = int(input("Enter choice: "))
            print("")

            if other_choice == 1:
                game()
            elif other_choice == 2:
                # show statistics from file
                if rps_file:
                    print(user_name, ", here are your game play statistics... ")
                    print("")
                    print("Wins: ", str(win_counter))
                    print("Loses: ", str(lose_counter))
                    print("Ties: ", str(tie_counter))

                    try:
                        ratio = format((win_counter / lose_counter), ".2f")
                        print("Win/Loss Ratio: " + ratio)
                        print("")
                    except:
                        print("Win/Loss Ratio: " + str(format(win_counter, ".2f")))
                        print("")
                else:
                    file_name = str(user_name + ".rps")
                    rps_file = open(file_name, "wb")

                    print(user_name, ", here are your game play statistics... ")
                    print("Wins: ", str(win_counter))
                    print("Loses: ", str(lose_counter))
                    print("Ties: ", str(tie_counter))

                    try:
                        ratio = format((win_counter / lose_counter), ".2f")
                        print("Win/Loss Ratio: " + str(ratio))
                        print("")
                    except:
                        print("Win/Loss Ratio: " + str(format(win_counter, ".2f")))
                        print("")

                continue
                
            elif other_choice == 3:
                #write results to file
                try: 
                    if rps_file:
                        stats = [user_name, win_counter, lose_counter, tie_counter]
                        pickle.dump(stats, rps_file)

                        #close file
                        rps_file.close()
                        print(user_name, ", your game has been saved.")
                    else:
                        file_name = str(user_name + ".txt")
                        rps_file = open(file_name, "wb")
                        stats = [user_name, win_counter, lose_counter, tie_counter]
                        pickle.dump(stats, rps_file)

                        #close file
                        rps_file.close()
                        print(user_name, ", your game has been saved.")
                    end = 1
                    continue
                except:
                    print("Sorry, " + user_name + ", the game could not be saved.")
        except:
            print("Please enter 1, 2, or 3.")

#main function
def main():
    while(True):
        try:
            global other_choice
            global user_name
            if other_choice == 3:
                break
            intro_choice = ""
            
            print("Welcome to Rock, Paper, Scissors!")
            print("")
            print("1. Start New Game")
            print("2. Load Game")
            print("3. Quit")
            print("")
            intro_choice = int(input("Enter choice: "))
            print("")

            if intro_choice == 1:
                print("")
                user_name = input("What is your name? ")
                print("")
                print("Hello, " + user_name + ". Let's play!")
                print("")
                game()
            elif intro_choice == 2:
                user_name = input("What is your name? ")
                print("")
                load_game()
                print("")
            elif intro_choice == 3:
                break
            else:
                "Please enter 1, 2, or 3."
                print("")
                continue
        except:
            print("Please enter 1, 2, or 3")
            print("")
            continue

#main function
main()