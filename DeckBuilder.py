import csv
import os

class DeckBuilder:

    def __init__(self):
        self.deck = dict()
        self.magic_build = dict()

    def _populate_database(self, file_path: str) -> bool:
        try:
            file_name = open(file_path)
            file_reader = csv.reader(file_name, delimiter=',')
            for row in file_reader:
                self.deck[row[0].upper()] = (row[1], 0)
            return True
        except:
            print("\n\n\nERROR:The file {} does not exist. Please check the spelling or the path of the file."
                  "\nMake sure that the full path is provided.".format(file_path))
            return False

    def _print_deck(self):
        number_of_items_on_screen = 0
        items_on_screen_limit = 10
        print('=' * 10, 'YOUR DECK', '=' * 10)

        for key in self.deck:
            print(key, ',', self.deck[key][0])
            number_of_items_on_screen += 1

            if number_of_items_on_screen == items_on_screen_limit:
                input("Press 'Enter' to show more...")
                number_of_items_on_screen = 0

        input("\n\n\nEnd of list.\nPress 'Enter' to continue...")

    def _add_card_to_deck_build(self, card_name: str, number_of_times: int) -> None:
        card_name = card_name.upper()

        if card_name in self.deck:
            if card_name in self.magic_build:
                self.magic_build[card_name] = (self.magic_build[card_name][0],
                                               self.magic_build[card_name][1] + number_of_times)
            else:
                self.magic_build[card_name] = (self.deck[card_name][0],
                                               self.deck[card_name][1] + number_of_times)
        else:
            print("Card {} does not exist in the database. "
                  "Please try another card or check the spelling.".format(card_name))

    def _decrease_number_of_occurrence(self, card_name: str, number_of_times: int) -> None:
        card_name = card_name.upper()

        if card_name in self.magic_build:
            if self.magic_build[card_name][1] - number_of_times >= 0:
                self.magic_build[card_name] = (self.magic_build[card_name][0],
                                               self.magic_build[card_name][1] - number_of_times)
            else:
                print("ERROR: Number provided more that the times that the card occurs in your build.\n"
                      "Accepted number for card {} is {}".format(card_name, self.magic_build[card_name][1]))

    def _remove_card_from_deck_build(self, card_name: str) -> None:
        card_name = card_name.upper()

        if card_name in self.magic_build:
            del self.magic_build[card_name]
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Card {} has been removed from your current build".format(card_name))
            input("\nPress 'Enter' to continue...")
        else:
            print("ERROR: Card {} does not exist in your current build.".format(card_name))

    def _print_current_build(self) -> None:
        number_of_items_on_screen = 0
        items_on_screen_limit = 10

        print('=' * 10, 'YOUR BUILD LIST', '=' * 10)
        for key in self.magic_build:
            print("{}: \t{}".format(key, (self.magic_build[key][0] * self.magic_build[key][1])))

            if number_of_items_on_screen == items_on_screen_limit:
                input("Press 'Enter' to show more...")
                number_of_items_on_screen = 0

        input("\n\n\nEnd of list.\nPress 'Enter' to continue...")

    def _write_current_build_to_file(self, directory_path: str, file_name: str) -> None:
        file_full_path =  directory_path + file_name + '.txt'
        file_to_write = open(file_full_path, 'w')
        sequence = ('=' * 30) + ' YOUR BUILD LIST ' + ('=' * 30) + "\n\n"

        for key in self.magic_build:
            # sequence += (key + " : " + ((self.deck[key][0] + " ") * self.deck[key][1]) + '\n')
            sequence += "{}: \t{}".format(key, (self.magic_build[key][0] * self.magic_build[key][1])) + "\n"

        file_to_write.write(sequence)
        file_to_write.close()
        print("Your file has been saved at this location:\n{}".format(file_full_path))

    def _is_database_empty(self) -> bool:
        if len(self.deck) == 0:
            return True
        return False


# db = DeckBuilder()
# db.populate_database("C:\\Users\\Stefanos\\Desktop\\MTGDB\\test.txt")
# db.add_card_to_deck_build("Parcelbeast", 3)
# db.add_card_to_deck_build("Huntmaster", 2)
# db.add_card_to_deck_build("cleric", 5)
# db.print_current_build()
# db.remove_card_from_deck_build("huntmaster")
# db.write_current_build_to_file("C:\\Users\\Stefanos\\Desktop\\MTGDB\\", "my build")
