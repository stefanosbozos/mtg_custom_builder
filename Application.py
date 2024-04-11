import sys

from DeckBuilder import DeckBuilder

class Application:

    _newDeck = DeckBuilder()

    def __init__(self):
        self._start()

    def _start(self) -> None:
        #self._show_header()
        self._main_menu()

    def _main_menu(self) -> None:
        while True:
            self._show_header()
            self._show_menu()
            user_input = input(">>")

            if user_input == '1':
                success = self._newDeck._populate_database(self._get_database())
                if not success:
                    print("Database has not been added.")

            elif user_input == '2':
                if not self._is_database_empty():
                    self._newDeck._print_deck()
                else:
                    print("\nERROR: You have not provided any database.\n")

            elif user_input == '3':
                if not self._is_database_empty():

                    card_name = input("\nPlease type the name of the card you want to add and press the 'Enter' key"
                                      "(e.g. Parcelbeast): ")
                    number_of_times = input("\nHow many times would you like to add this card to your build"
                                            " (Press enter to confirm): ")
                    self._newDeck._add_card_to_deck_build(card_name, int(number_of_times))
                else:
                    print("\nERROR: You have not provided any database.\n")

            elif user_input == '4':
                if not self._is_database_empty():
                    card_name = input("\nPlease type the name of the card you want to decrease "
                                      "the number of occurrences in your build and press the 'Enter' key"
                                      "(e.g. Parcelbeast): ")
                    number_of_times = input("\nHow many times would you like to decrease this card's "
                                            "occurrence in your build (Press enter to confirm): ")
                    self._newDeck._decrease_number_of_occurrence(card_name, int(number_of_times))
                else:
                    print("\nERROR: You have not provided any database.\n")

            elif user_input == '5':
                if not self._is_database_empty():
                    card_name = input("\nType in the name of the card you want to remove:")
                    self._newDeck._remove_card_from_deck_build(card_name)
                else:
                    print("\nERROR: You have not provided any database.\n")

            elif user_input == '6':
                if not self._is_database_empty():
                    self._newDeck._print_current_build()
                else:
                    print("ERROR: You have not provided any database.")

            elif user_input == '7':
                if not self._is_database_empty():
                    confirmation = input("\nAre you sure you want to save this build? (y/n):")
                    if confirmation == 'y':
                        directory_path = input("\nType in the full path of the folder that you "
                                               "want to save your build."
                                               "(e.g C:\\Users\\yourUserName\\Desktop\\):")
                        file_name = input("\nType the name of the file (e.g. My Deck Build): ")
                        self._newDeck._write_current_build_to_file(directory_path, file_name)
                    else:
                        continue
                else:
                    print("\nERROR: You have not provided any database.\n")

            elif user_input == '8':
                confirmation = input("\nAre you sure you want to exit? (y/n):")
                if confirmation == 'y':
                    return
                else:
                    continue

            else:
                print("\nWrong Input...\nPlease select a number from 1 to 6 as indicated in the menu.")

        sys.exit()

    def _get_database(self) -> str:
        return input("Enter the full path to your database "
                     "(e.g. C:\\Users\\myUserName\\Documents\\myDatabase.txt). "
                     "The file must be in either .txt or .csv format.:")

    def _is_database_empty(self) -> bool:
        return self._newDeck._is_database_empty()

    def _show_menu(self) -> None:
        print("\n1. Add a new card database\n"
              "2. Show your card database\n"
              "3. Add a card to your build\n"
              "4. Remove card's occurrence from current build\n"
              "5. Remove card from current build\n"
              "6. Show your current build\n"
              "7. Write current build\n"
              "8. Exit Application\n")

    def _show_header(self) -> None:
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