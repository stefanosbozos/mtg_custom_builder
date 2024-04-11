import sys
import os

from DeckBuilder import DeckBuilder

class Application:

    """
    This class provides functionality for showing the menus and the overall
    application loop, until the user selects to exit.

    @Author: Stefanos Bozos
    @Version: 0.0.1 build 20240412
    """

    _newDeck = DeckBuilder()        # Stores the user's card database

    def __init__(self):
        self.__main_menu()

    def __main_menu(self) -> None:
        """
        Implementation of the menu options.
        """
        while True:
            self.__render_menu()
            user_input = input(">>")

            if user_input == '1':
                self.__database_initialization()
            elif user_input == '2':
                self.__print_database()
            elif user_input == '3':
                self.__add_card_to_deck()
            elif user_input == '4':
                self.__decrease_number_of_specific_card()
            elif user_input == '5':
                self.__remove_card_from_deck()
            elif user_input == '6':
                self.__print_deck()
            elif user_input == '7':
                self.__save_deck_to_txt()
            elif user_input == '8':
                self.__exit_application()
            else:
                print("\nWrong Input...\nPlease select a number from 1 to 6 as indicated in the menu.")

    def __render_menu(self) -> None:
        """
        Renders the header and the main menu in the terminal window.
        """
        self.__clear_screen()
        self.__show_header()
        self.__show_menu()

    def __exit_application(self) -> None:
        """
        Terminates the application. Asks the user first for confirmation.
        """
        self.__clear_screen()
        confirmation = input("\nAre you sure you want to exit? (y/n):")
        if confirmation == 'y':
            sys.exit()

    def __save_deck_to_txt(self) -> None:
        """
        Provided a path and a file name, the new deck is being saved in .txt format.
        """
        if not self.__is_database_empty():
            self.__clear_screen()
            confirmation = input("\nAre you sure you want to save this build? (y/n):")
            if confirmation == 'y':
                directory_path = input("\nType in the full path of the folder that you "
                                       "want to save your build."
                                       "(e.g C:\\Users\\yourUserName\\Desktop\\):")
                file_name = input("\nType the name of the file (e.g. My Deck Build): ")
                self._newDeck.__write_current_build_to_file(directory_path, file_name)
        else:
            print("\nERROR: You have not provided any database.\n")
        self.__continue_to_next_screen()

    def __print_deck(self) -> None:
        """
        Prints the deck that the user has put together so far.
        """
        if not self.__is_database_empty():
            self._newDeck.__print_current_build()
        else:
            print("ERROR: You have not provided any database.")
            self.__continue_to_next_screen()

    def __remove_card_from_deck(self) -> None:
        """
        Removes a card from the deck that the user has built so far completely.
        """
        self.__clear_screen()
        if not self.__is_database_empty():
            card_name = input("\nType in the name of the card you want to remove:")
            self._newDeck.__remove_card_from_deck_build(card_name)
        else:
            print("\nERROR: You have not provided any database.\n")
            self.__continue_to_next_screen()

    def __decrease_number_of_specific_card(self) -> None:
        """
        Removes a number of occurrences of a certain card in the
        deck that the user has built so far.
        """
        if not self.__is_database_empty():
            card_name = input("\nPlease type the name of the card you want to decrease "
                              "the number of occurrences in your build and press the 'Enter' key"
                              "(e.g. Parcelbeast): ")
            number_of_times = input("\nHow many times would you like to decrease this card's "
                                    "occurrence in your build (Press enter to confirm): ")
            self._newDeck.__decrease_number_of_occurrence(card_name, int(number_of_times))
        else:
            print("\nERROR: You have not provided any database.\n")

    def __add_card_to_deck(self) -> None:
        """
        Adds card to the deck that the user is currently building.
        """
        self.__clear_screen()
        if not self.__is_database_empty():

            card_name = input("\nPlease type the name of the card you want to add and press the 'Enter' key"
                              "(e.g. Parcelbeast): ")
            number_of_times = input("\nHow many times would you like to add this card to your build"
                                    " (Press enter to confirm): ")
            self._newDeck.__add_card_to_deck_build(card_name, int(number_of_times))
        else:
            print("\nERROR: You have not provided any database.\n")
        self.__continue_to_next_screen()

    def __print_database(self) -> None:
        """
        Prints the card database that the user has provided.
        """
        if not self.__is_database_empty():
            self._newDeck.__print_deck()
        else:
            print("\nERROR: You have not provided any database.\n")
            self.__continue_to_next_screen()

    def __database_initialization(self) -> None:
        """
        Creates a new card database from the given file in .txt or .csv form
        from the user.
        """
        success = self._newDeck.__populate_database(self.__get_database())
        if not success:
            print("Database has not been added.")
            self.__continue_to_next_screen()

    def __get_database(self) -> str:
        """
        Requests the user to provide a path where the card database is located.
        :return: A string of a full file path.
        """
        return input("Enter the full path to your database "
                     "(e.g. C:\\Users\\myUserName\\Documents\\myDatabase.txt). "
                     "The file must be in either .txt or .csv format.:")

    def __is_database_empty(self) -> bool:
        """
        Checks if the user has provided successfully a card database.
        :return: A boolean True or False
        """
        return self._newDeck.__is_database_empty()

    def __clear_screen(self) -> None:
        """
        Clears the terminal screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def __continue_to_next_screen(self) -> None:
        """
        Pauses the control flow by requesting a simple input so the user can read the program's output,
        before giving control back to the program.
        """
        input("\n\nPress 'Enter' to continue")

    def __show_menu(self) -> None:
        """
        Renders the main menu with all the actions that the user can do.
        """
        print("\n1. Add a new card database\n"
              "2. Show your card database\n"
              "3. Add a card to your build\n"
              "4. Remove card's occurrence from current build\n"
              "5. Remove card from current build\n"
              "6. Show your current build\n"
              "7. Write current build\n"
              "8. Exit Application\n")

    def __show_header(self) -> None:
        """
        Shows the banner header of the application.
        """
        print("""
#############################################################################################
#  ___  ___            _         ______          _       ______       _ _     _             #
#  |  \/  |           (_)        |  _  \        | |      | ___ \     (_) |   | |            #
#  | .  . | __ _  __ _ _  ___    | | | |___  ___| | __   | |_/ /_   _ _| | __| | ___ _ __   #
#  | |\/| |/ _` |/ _` | |/ __|   | | | / _ \/ __| |/ /   | ___ \ | | | | |/ _` |/ _ \ '__|  #
#  | |  | | (_| | (_| | | (__    | |/ /  __/ (__|   <    | |_/ / |_| | | | (_| |  __/ |     #
#  \_|  |_/\__,_|\__, |_|\___|   |___/ \___|\___|_|\_\   \____/ \__,_|_|_|\__,_|\___|_|     #
#                 __/ |                                                                     #
#                |___/                                                                      #
#############################################################################################                                                                                                                              
     """)