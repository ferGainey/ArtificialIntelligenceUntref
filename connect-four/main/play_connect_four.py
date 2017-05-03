from connect_four_board import ConnectFourBoard
import os

def main():
    connect_four = ConnectFourBoard()
    menu_choice = 1
    while menu_choice == 1:
        os.system(['clear', 'cls'][os.name == 'nt'])
        # start the game
        start_choice = -1
        while start_choice != 1 and start_choice != 2:
            print("Start")
            print("1) Move first")
            print("2) Move second")
            start_choice = int(raw_input("choice : "))
            if start_choice != 1 and start_choice != 2:
                print ("This option does not exist")
                print ("\n\n\n")
        connect_four.start_new(start_choice)
        # menu
        print("Menu")
        print("1) Play again")
        print("2) Quit")
        menu_choice = int(raw_input("choice : "))


if __name__ == "__main__":
    main()
