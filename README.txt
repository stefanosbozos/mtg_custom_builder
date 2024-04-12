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

version 0.0.1 build 20240412
Author Stefanos Bozos

Magic Deck Builder is a deck builder for custom Magic The Gathering builds. Its main functionality
is that it takes a card database in the form of either .csv or .txt that contain the cards in the form
<card name>,<card code>. The user can add a card from the give database to their build, select the number
of times that they want this card to be added to the build, decrease the times that a card occurs in the
build, remove a card from the current build, and finally save the build into a separate .txt file.


HOW TO USE:

First you need to provide the program with a card database. (Option 1 from the menu) Otherwise,
you will get an error that there is not any database and no further actions can be done. The
database is in the form of either .csv or .txt. The items in the database should be in the form
below, in order to get correct results.

<card name>,<card code>

After you provide a card database, you can use the option listed in the main menu to add cards to
your build from the given database. On the build you can do the below actions:

- Add a new card
- Remove a card
- Remove the times that a card occurs in the build
- Show the given card database
- Show the current created build
- Save the current build to a .txt file


ADD A CARD DATABASE:
The program will ask you to provide the path to the .txt or .csv file that your card database is
stored. *IMPORTANT* You need to write down the full path and file extension otherwise the database
will fail to be added.

Example:
C:\Users\user1\Desktop\my_card_database.txt


ADD A CARD TO YOUR BUILD:
The program asks you to type in the name of the card you want to add. If the card exists, then you
will be asked the number of times that this card should be added to the build. After the card is
successfully added you will get a confirmation.

*IMPORTANT* The number of times should be greater than 0. If you give either a negative number or 0
the card will not be added.


REMOVE A CARD FROM YOUR BUILD:
The program asks you to type in the name of the card you want to remove. If the card exists, the card
will be deleted from your current build completely. If the process is successful you will get a confirmation
on the terminal screen.


REMOVE A CARD'S NUMBER OF OCCURRENCE:
This option remove the number that a card occurs in your build. For example, you have added the card
'Huntmaster Liger' 4 times (occurrences), and you actually need this card 2 times in the build instead.
With this option you can type in how many times you want to remove this card from the build. This operation
does not receive negative numbers.


SAVE YOUR BUILD TO A FILE:
The program asks you to provide a path and a name for you file. The file should be the full path in order to save
the file in the correct directory. If no path is given the file will be saved at the same directory as the
Magic_Deck_Builder.exe. The name of the file should be WITHOUT the extension. If accidentally you type the extension
the .txt will be added to your file name.

Examples:
C:\Users\user1\Desktop\ (make sure not to forget the final \)

my_new_build OR my new build (The extension will be added automatically. Also, the file name can contain whitespaces)


FUTURE UPDATES:
- In future versions of the application the option of saving the database for future use as well as providing a new
database everytime.
- More filetypes to be supported (e.g. mySQL databases)
- GUI for better navigation and use


***

For any bug, issues or feature requests, please create an issue at:

https://github.com/stefanosbozos/mtg_custom_builder/issues

***


Thank you for using this application.