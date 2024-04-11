import csv
import os

class DeckBuilder:
    """
    It holds all the operations that can be performed on the current deck build.
    The operations that this class contains are to create a new card database,
    populate it, print the card database, create and add a new card to the user's
    deck build, remove a card from the deck build, show the deck build, and
    save that build to a file.

    @Author: Stefanos Bozos
    @Version: 0.0.1 build 20240412
    """

    def __init__(self):
        self.deck = dict()                  # Stores the user's database
        self.magic_build = dict()           # Stores the user's created card build

    def _populate_database(self, file_path: str) -> bool:
        """
        Populates the card database with the given items of a .csv or .txt file.
        The input should only be comma separated values in order to provide correct output.

        :param file_path: A string that contains the full path to the .csv or .txt file
        :return: A boolean True or False to confirm if the file exist and the database has been added successfully.
        """
        try:
            self.__read_file(file_path)
            return True
        except:
            self.__clear_screen()
            print("\n\n\nERROR:The file {} does not exist. Please check the spelling or the path of the file."
                  "\nMake sure that the full path is provided.".format(file_path))
            return False

    def __read_file(self, file_path: str) -> None:
        """
        Read a .csv or .txt file and stores the first element of the line as
        the key of the card database dictionary, the second element as a value,
        and adds an integer set to 0 to initialize how many times the card has been added
        to the current build.

        :param file_path:  string that contains the full path to the .csv or .txt file
        """
        file_name = open(file_path)
        file_reader = csv.reader(file_name, delimiter=',')
        for row in file_reader:
            self.deck[row[0].upper()] = (row[1], 0)

    def _print_deck(self) -> None:
        """
        Prints all the elements of the provided card database. The elements
        are being showed 10 at a time.
        """
        number_of_items_on_screen = 0
        items_on_screen_limit = 10

        self.__clear_screen()
        print('=' * 10, 'YOUR DECK', '=' * 10)
        for key in self.deck:
            print(key, ',', self.deck[key][0])
            number_of_items_on_screen += 1

            if number_of_items_on_screen == items_on_screen_limit:
                input("Press 'Enter' to show more...")
                number_of_items_on_screen = 0

        input("\n\n\nEnd of list.\nPress 'Enter' to continue...")

    def _add_card_to_deck_build(self, card_name: str, number_of_times: int) -> None:
        """
        Adds a new card to the current build. The card name is the key, and the value
        is a tuple containing the card code and the number that this card occurs in the
        build.

        :param card_name: A string containing the card name that
        we want to add to the current build from the card database

        :param number_of_times: An integer representing the number of times that we want to add the card.
        """
        card_name = card_name.upper()

        if card_name in self.deck:
            if card_name in self.magic_build:
                self.magic_build[card_name] = (self.magic_build[card_name][0],
                                               self.magic_build[card_name][1] + number_of_times)
            else:
                self.magic_build[card_name] = (self.deck[card_name][0],
                                               self.deck[card_name][1] + number_of_times)
        else:
            self.__clear_screen()
            print("Card {} does not exist in the database. "
                  "Please try another card or check the spelling.".format(card_name))

    def _decrease_number_of_occurrence(self, card_name: str, number_of_times: int) -> None:
        """
        Decreases the times that a card is being repeated from the build by as given number
        from the user. The given number should not be greater than the card number of occurrences.

        :param card_name: A string representing the card name from the current deck build that we want to apply the change.
        :param number_of_times: The number of occurrences of the card that we want to subtract.
        """
        self.__clear_screen()
        card_name = card_name.upper()

        if card_name in self.magic_build:
            if (self.magic_build[card_name][1] + 1) > number_of_times:
                self.magic_build[card_name] = (self.magic_build[card_name][0],
                                               self.magic_build[card_name][1] - number_of_times)

                print("Card {} occurrence has decreased to {}.\n{}: \t{} ".format(
                    card_name,
                    self.magic_build[card_name][1],
                    card_name,
                    self.magic_build[card_name][0]
                ))
            elif self.magic_build[card_name][1] == number_of_times:
                self._remove_card_from_deck_build(card_name)
            else:
                print("ERROR: Number provided more that the times that the card occurs in your build.\n"
                      "Accepted number for card {} is {}".format(card_name, self.magic_build[card_name][1]))

        self.__continue_to_next_screen()

    def _remove_card_from_deck_build(self, card_name: str) -> None:
        """
        Completely removes a card from the current deck build.

        :param card_name: A string representing the card from the current build that we want to remove.
        """
        card_name = card_name.upper()
        self.__clear_screen()

        if card_name in self.magic_build:
            del self.magic_build[card_name]
            print("Card {} has been removed from your current build".format(card_name))
        else:
            print("ERROR: Card {} does not exist in your current build.".format(card_name))

        self.__continue_to_next_screen()

    def _print_current_build(self) -> None:
        """
        Prints the add card with their codes that the user has added so far in the
        current deck build.
        """
        self.__clear_screen()

        number_of_items_on_screen = 0
        items_on_screen_limit = 10

        print('=' * 10, 'YOUR BUILD LIST', '=' * 10)
        for key in self.magic_build:
            print("{} :\t {}".format(key, (self.magic_build[key][0] + " ") * self.magic_build[key][1]))

            if number_of_items_on_screen == items_on_screen_limit:
                input("Press 'Enter' to show more...")
                number_of_items_on_screen = 0

        input("\n\n\nEnd of list.\nPress 'Enter' to continue...")

    def _write_current_build_to_file(self, directory_path: str, file_name: str) -> None:
        """
        Saves the current deck build to a .txt file. The path and the name of the file
        are being provided by the user.

        :param directory_path: A string representing the directory that the user wants to save the file.
        :param file_name: A string representing the name that the user wants to give to the file.
        """
        file_full_path =  directory_path + file_name + '.txt'
        file_to_write = open(file_full_path, 'w')
        sequence = ('=' * 30) + ' YOUR BUILD LIST ' + ('=' * 30) + "\n\n"

        for key in self.magic_build:
            sequence += "{}: \t{} ".format(key, (self.magic_build[key][0] + " ") * self.magic_build[key][1]) + "\n"

        file_to_write.write(sequence)
        file_to_write.close()
        print("\n\nYour file has been saved at this location:\n{}".format(file_full_path))

    def _is_database_empty(self) -> bool:
        """
        Checks if the user has provided a card database.
        :return: A boolean True if the card database length is not 0
        """
        if len(self.deck) == 0:
            return True
        return False
    def __clear_screen(self) -> None:
        """
        Clears the terminal screen
        """
        os.system('cls' if os.name == 'nt' else 'clear')
    def __continue_to_next_screen(self) -> None:
        """
        Pauses the control flow by requesting a simple input so the user can read the program's output,
        before giving control back to the program.
        """
        input("\n\nPress 'Enter' to continue")