import os
from blackjack_game import BlackjackGame

def main():
    blackjack = BlackjackGame()
    menu_choice = 1
    while menu_choice == 1:
        os.system(['clear', 'cls'][os.name == 'nt'])
        # start the game
        start_choice = -1
        while start_choice != 1 and start_choice != 2:
            print("Menu")
            print("1) Play")
            print("2) Quit")
            start_choice = int(raw_input("choice : "))
            if start_choice != 1 and start_choice != 2:
                print ("This option does not exist")
                print ("\n\n\n")
            if start_choice == 2:
                exit()
        if start_choice == 1:
            os.system(['clear', 'cls'][os.name == 'nt'])
            print("Edit")
            number_of_training = int(raw_input("Number of training : "))
            number_of_real_rounds = int(raw_input("Number of real rounds : "))
            blackjack.start_game(number_of_training, number_of_real_rounds)
        # menu
        print("\n\n1) Continue")
        print("2) Quit")
        menu_choice = int(raw_input("choice : "))


if __name__ == "__main__":
    main()