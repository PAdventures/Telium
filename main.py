# Importing useful packages

from time import *  # To use the sleep() procedure to make the program run smoother
from random import *  # Use for randomising certain things such as chances
from math import * # Handle damage rounding
import os  # Useage for using commands in the terminal
import sys  # Exiting the program


# Global Variables

gamemode = "" # The gamemode the player is in
num_modules = 0  # The number of modules in the current station
station = "" # The name of the station that the player is in
curr_module = 1  # The number of the current module that the player is in
last_module = 0  # The number of the last module the player was in
possible_moves = []  # The modules that the player can move to
curr_deck = ""  # The letter of the deck the player is in
curr_room = ""  # The module description of the player's current module
alive = True  # Is the player alive
won = False  # Has the player won
hp = 100  # Player health
defence = 10  # Player defence
damage_reduction = 0 # The damage reduction percentage
damage_increase = 50 # The damage increase percentage
power = 100  # The amount of power the space station has
fuel = 500  # The amount of fuel the player has to use their flamethrower
locked = 0  # The module that is locked by the player
queen = 0  # The module that the alien queen is in
vent_shafts = []  # The modules where vent shafts are located in
info_panels = []  # The modules where information panels are located in
workers = []  # The modules where alien workers are located in

# Procedure declarations

# Displays the story of the game to the player
def display_story():
    # Clears the console
    os.system("clear")

    # The story paragraphs
    paragraph1 = "A remote probe on the surface of Mars has detected biological signatures of dormant, single-celled, primative life. A sample of the Martian soil is returned to a space station orbiting the Earth for further analysis."
    paragraph2 = "The orange-coloured cells are examined and DNA analysis shows remarkable similarities to Dictyostelium discoideum, a species of soil-living amoeba from Earth. Commonly referred to as slime mould, it transitions from a collection of unicellular amoebae into a multicellular organism and then into a fruiting body."
    paragraph3 = "Nicknamed Telium due to its colour and cellular structure, the sample is incubated in a lab with conditions similar to Mars' ancient past when it was a warmer, wetter planet."
    paragraph4 = "Remarkably, independant Telium cells slowly begin to move and, after a period of several days, join together to form an organism resembling a slug. In the coming days, the creature grows additional arms and begins to look like a large startfish. Intrigued, scientists continue to examine the creature, which appears to be consuming bacteria from inside the incubation chamber and growing in size with each passing day."
    paragraph5 = "Telium begins to show signs of advanced movement around the chamber, and its strength increases significantly. Eventually, it becomes strong enough to break out of its chamber and suffocates a scientist. The creature scuttles through the space station to an unknown location."
    paragraph6 = "Telium is not seen for several days."
    paragraph7 = "Tension between the astonauts escalates when electronics on the station begin to behave erratically, power starts draining and communication at central command with Earth is lost."
    paragraph8 = "Clearly this is the work of Telium, the Queen Alien."
    paragraph9 = "\"We are on our own. Telium must be found and destroyed,\" the captain orders. \"There is no protocol for this, but we cannot risk further loss of life. We must stick together and work it out.\""

    # Printing the paragraphs character by character with an X second delay then wait Y seconds before printing the next paragraph
    for char in paragraph1:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.05)

    print("\n")
    for char in paragraph2:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.05)

    print("\n")
    for char in paragraph3:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.05)

    print("\n")
    for char in paragraph4:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.05)

    print("\n")
    for char in paragraph5:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.05)

    print("\n")
    for char in paragraph6:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.05)

    print("\n")
    for char in paragraph7:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.05)

    print("\n")
    for char in paragraph8:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.05)

    print("\n")
    for char in paragraph9:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.05)
    option = 0
    while option not in ("r", "return"):
        os.system('clear')
        print(paragraph1)
        print('\n')
        print(paragraph2)
        print('\n')
        print(paragraph3)
        print('\n')
        print(paragraph4)
        print('\n')
        print(paragraph5)
        print('\n')
        print(paragraph6)
        print('\n')
        print(paragraph7)
        print('\n')
        print(paragraph8)
        print('\n')
        print(paragraph9)
        print('\n\n')
        print("-----------------------------------------------------------------")
        option = input("(R)eturn to help menu: ")
    os.system('clear')

# Shows an error that occured (Dev usage only)
def render_error(custom_code, message, timeout = 5):
    # Continue to update the message until the timer has reached -1
    while timeout != -1:
        # Clear the consle
        os.system('clear')
        # Show a nice formated error message
        print("-----------------------------------------------------------------")
        print("Error: {0}".format(custom_code))
        print("Message: {0}".format(message))
        print("-----------------------------------------------------------------")
        print("Stopping game in {0} seconds".format(timeout))
        # Decrease timer by 1
        timeout -= 1
        # Wait 1 second
        sleep(1)
    # Cleat the console
    os.system('clear')
    # Stop the python file
    sys.exit()

# Display specified information in text files found in "Help_Text"
def handle_help_text_file_rendering(type="", code=""):
    # If the type given is not valid, display an error
    if type != "query":
        # Stop the function and send error info to the renderer
        return render_error("TYPENOTFOUND", "Param \"type\" given in help text file rendering does not exist", 5)
    # Open the text file to read it using corresponding to the type of info and the info code
    text_file = open("Help_Text/{0}_{1}.txt".format(type, code), 'r')
    # Clear to console if there is anything being displayed
    os.system('clear')
    # Read the text file and print it to the console
    print(text_file.read())
    # Display a clean return to menu option
    print("\n")
    print("-----------------------------------------------------------------")
    # Ask the user to type "r" or "return"
    option = input("(R)eturn to help menu: ")
    # Force the input to become lower cased
    option = option.lower()
    # If the correct input was proved, stop the function and show the help menu
    if option == "r" or option == "return":
        return display_help()
    # Stop and re-call the function
    else:
        return handle_help_text_file_rendering(type, code)
    
# Prints the game instructions to beat the game
def display_instructions():
    # Clear the console
    os.system('clear')
    # Print the instuctions
    print("1. To win you must find and kill the Alien Queen, Telium, by blocking all of it's exits and killing it with your flamethrower")
    print("2. You can use the commands M(2) or MOVE(2) to move to a connecting module next to your current module")
    print("3. Alien workers are placed randomly around the station and can cause you trouble")
    print("4. Ventilation shafts will randomly move around the station")
    print("5. You can lock 1 module at a time to block the aliens")
    print("6. If you run out of health or the staion runs out of power you die\n")
    print("-----------------------------------------------------------------")
    # Ask the user for input
    option = input("(R)eturn to menu: ")
    # Force the input to become lower cased
    option = option.lower()
    # If the correct input was given, stop the function and show the main menu
    if option == "r" or option == "return":
        return show_title_screen()
    # Stop and re-call the function
    else:
        return display_instructions()

# Shows the help menu
def display_help():
    # Declare a variable to force the while loop to start
    option = 0
    # Continue to loop in the "option" variable is not in the list below
    while option not in ("aq", "wa", "vs", "ip", "lm", "mc", "ss", "ps", "r"):
        # Clear the console
        os.system('clear')
        # Show the help menu
        print("-----------------------------------------------------------------")
        print("Alien Queen - (AQ)")
        print("Worker Aliens - (WA)")
        print("Ventilation Shafts - (VS)")
        print("Information Panels - (IP)")
        print("Locking Modules - (LM)")
        print("Movment Controlls - (MC)")
        print("Station Stats - (SS)")
        print("Player Stats - (PS)")
        print("-----------------------------------------------------------------")
        print("Return to menu - (R)")
        print("-----------------------------------------------------------------\n")
        print("Welcome to the help menu. Please type one of the option codes which can be seen around brackets")
        # Ask the user for input
        option = input("> ")
        # Force the input to become lower cased
        option = option.lower()
    # If the input is "r", stop the function and show the main menu
    if option == "r":
        return show_title_screen()
    # Stop the function and send data to the help text file handler
    return handle_help_text_file_rendering("query", option)

# Manage easy mode
def handle_easy_mode():
    # Allow global variables to be changed
    global gamemode, num_modules, station, damage_reduction, hp, defence, fuel, power
    # Change the global variables to match the easy mode settings
    gamemode = "Easy"
    num_modules = 17
    station = "Victoria_Station"
    damage_reduction = 50
    hp = 150
    defence = 20
    fuel = 750
    power = 150

# Manage normal mode
def handle_normal_mode():
    # Allow global variables to be changed
    global gamemode, num_modules, station, damage_reduction
    # Change the global variables to match the normal mode settings
    gamemode = "Normal"
    num_modules = 20
    station = "Charles_Darwin"
    damage_reduction = 0

# Manage hard mode
def handle_hard_mode():
    # Allow global variables to be changed
    global gamemode, num_modules, station, damage_increase, defence
    # Change the global variables to match the hard mode settings
    gamemode = "Hard"
    num_modules = 30
    station = "Iris"
    damage_increase = 50
    defence = 5

# Manage impossible mode
def handle_impossible_mode():
    # Allow global variables to be changed
    global gamemode, num_modules, station, damage_increase, hp, defence, fuel, power
    # Change the global variables to match the impossible mode settings
    gamemode = "Impossible"
    num_modules = 50
    station = "Olympus"
    damage_increase = 100
    hp = 50
    defence = 0
    fuel = 250
    power = 50

# Show all gamemodes to play in
def show_gamemodes():
    # Declare a variable to force the while loop to start
    option = 0
    # Continue to loop in the "option" variable is not in the list below
    while option not in ("easy", "e", "normal", "n", "hard", "h", "impossible", "i"):
        # Clear the console
        os.system('clear')
        # Show all gamemodes
        print("-----------------------------------------------------------------")
        print("Easy Mode (E) - Start with 50% more health, less damage taken, more defence, less modules")
        print("Normal Mode (N) - All settings are default")
        print("Hard Mode (H) - More damage taken, less defence, more modules")
        print("Impossible Mode (I) - Start with 50% less health, more damage taken, no defence, more modules")
        print("-----------------------------------------------------------------\n")
        print("Type the gamemode you want to play in. If you're new, it is recommened you play normal mode")
        # Ask the user for input
        option = input("> ")
        # Force the input to become lower cased
        option = option.lower()
    # If the option matches the correct gamemode code, change global settings and stop the function
    if option == "easy" or option == "e":
        handle_easy_mode()
    elif option == "normal" or option == 'n':
        handle_normal_mode()
    elif option == "hard" or option == "h":
        handle_hard_mode()
    elif option == "impossible" or option == "i":
        handle_impossible_mode()
    # Or if the code gets confused and the loop is stopped with the input being inncorrect, stop and re-call the function
    else:
        return show_gamemodes()
    return

# Show the main menu
def show_title_screen():
    # Declare a variable to force the while loop to start
    option = 0
    # Continue to loop in the "option" variable is not in the list below
    while option not in ("play", "p", "story", "s", "help", "h", "instructions", "i", "quit", "q"):
        # Clear the console
        os.system("clear")
        # Show the menu options
        print("-----------------------------------------------------------------")
        print("Play (P)\nStory (S) - Recommended\nHelp (H) - Ask a query on a game machanic\nInstructions (I) - How to play\nQuit (Q)")
        print("-----------------------------------------------------------------\n")
        print("Type the option you would like to select")
        # Ask the user for input
        option = input("> ")
        # Force the input to become lower cased
        option = option.lower()
    # If the input matches the correct code, stop and start the gamemode display
    if option == "play" or option == "p":
        return show_gamemodes()
    # Or show the story line and then stop and re-call the function
    elif option == "story" or option == "s":
        display_story()
        return show_title_screen()
    # Or stop the function and show the help menu
    elif option == "help" or option == "h":
        return display_help()
    # Or stop the function and show the instructions
    elif option == "instructions" or option == "i":
        return display_instructions()
    # Or clear the console and stop the python file
    elif option == "quit" or option == "q":
        os.system("clear")
        sys.exit()
    # And in case of a weird error, clear the console and stop the python file
    else:
        os.system("clear")
        sys.exit()

# Get the players current module data
def load_module():
    # Allow global variables to be changed
    global curr_module, possible_moves, curr_deck, curr_room
    # Get the module data as an array
    module = get_modules_from(curr_module)
    # Change the global variables according to the returned data
    possible_moves = module[0]
    curr_deck = module[1]
    curr_room = module[2]
    # Stop and show the module as a neat display
    return output_module()

# Get the data from the module's text file
def get_modules_from(module):
    # The modules connecting the "module"
    moves = []
    # The location of the "modue"
    deck = ""
    # The name of the "module"
    room = ""
    # If "station" is not correcly named, stop the function and render an error
    if (station not in ('Charles_Darwin', 'Victoria_Station', 'Iris', 'Olympus')):
        return render_error('STNNOTFOUND', 'The station name was not found and is currenly named as: {0}'.format(station))
    # Open the text file of the "module" in the current gamemode station
    text_file = open("Stations/" + station + "/module" + str(module) + ".txt", "r")
    # Loop and read all 6 lines
    for counter in range(0, 6):
        # Read the current line
        move_read = text_file.readline()
        # If "counter" is 4, which means this is line 5
        if counter == 4:
            # Change the "deck" to the line which is stripped to prevent "\n" being added to the variable
            deck = move_read.strip()
        # If "counter" is 5, which means this is line 56
        elif counter == 5:
            # Change the "room" to the line which is stripped to prevent "\n" being added to the variable
            room = move_read.strip()
        # Then the line is a number to show connecting modules
        else:
            # Stip and change the line to a number
            move_read = int(move_read.strip())
            # If "move_read" is not 0, add it to the "moves" array
            if move_read != 0:
                moves.append(move_read)
    # Close the "module" text file
    text_file.close()
    # Return the cleaned "module" data as an array
    return moves, deck, room

# Re-load a module
def reload_module():
    # Clear the console
    os.system('clear')
    # Show the current module
    output_module()
    # Check if the queen needs to move
    move_queen()
    # Show the possible moves
    output_moves()
    # Ask the user for an action to perform
    get_action()

# Display the current module as a neat output
def output_module():
    # Clear the console
    os.system('clear')
    # Show the current module data as a display
    print("-----------------------------------------------------------------\n")
    print(curr_deck + " >>> " + curr_room)
    print()
    print("You are in module", curr_module)
    print("\n-----------------------------------------------------------------\n")

# Show the modules the player can move to
def output_moves():
    # Print the modules the player can move to on one line neatly
    print("\nFrom here you can move to modules: | ", end=' ')
    for move in possible_moves:
        print(move, ' | ', end=' ')
    print()

# Ask the user to make an action
def get_action():
    # Allow global variable to be changed
    global curr_module, last_module, possible_moves, power
    # Delare a variable to force the loop to start
    valid_action = False
    # Continue to loop if "valid_action" does not change to True
    while valid_action != True:
        # Display what actions the player can do
        print("What do you want to do next ?")
        print("\n- (M)OVE - Optional syntax include module number moving to || Example: M2 or MOVE2")
        print("- (S)CANNER")
        # Ask the user for input
        action = input("> ")
        # Force the input to become upper cased
        action = action.upper()
        # Wait 1 second
        sleep(1)
        # If the input equals an "M" as the first character check for correct inputing format to move the player
        if action.find("M") == 0:
            # Delare a variable to be used in all indentations
            move = ""
            # If the input equal "M" or "MOVE"
            if action == "M" or action == "MOVE":
                # Ask the user for more input
                print("Enter the module to move to or go back to the actions || Example: 2 or B or BACK")
                move = input("> ")
                # Force the input to become lower cased
                move = move.lower()
            # If the input length equals 2
            if len(action) == 2:
                # Turn the input into an array of all characters
                actionArray = list(action)
                # Check if the last array item is a number
                if (actionArray[1].isdigit()):
                    # If it is, make "move" into this number
                    move = int(actionArray[1])
            # If the input length equals 5 and it starts with "MOVE"
            if len(action) == 5 and action.startswith("MOVE"):
                # Turn the input into an array of all characters
                actionArray = list(action)
                 # Check if the last array item is a number
                if (actionArray[4].isdigit()):
                    # If it is, make "move" into this number
                    move = int(actionArray[4])
            # If the input or "move" equals "back" or "b"
            if action == "back" or action == "b" or move == "back" or move == "b":
                # Stop the function and reload the module
                return reload_module()
            # If the variable "move" is a string
            elif str(move).isnumeric() == False:
                # Stop the function and reload the module
                return reload_module()
            # If "move" is a number and it is in the "possible_moves" array
            elif int(move) in possible_moves:
                # Allow the loop to end
                valid_action = True
                # Change the global variables
                last_module = curr_module
                curr_module = move
                power -= 1
                # If there is no power left in the station
                if power <= 0:
                    # Set the player to no longer be alive and then stop the function
                    alive == False
                    return
            # Or if the "move" is not in "possible_moves"
            else:
                # Wait 1 second
                sleep(1)
                # Tell the player that the module they want to move to must be connected to the current module
                print("\n\nThe module must be connected to the current module.")
                # Wait 3 more seconds
                sleep(3)
                # Stop the function and re-load the module
                return reload_module()
        # If the input equals an "S" as the first character check for correct inputing format to open the scanner
        if action.find("S") == 0:
            # Declare a variable to force the while loop to start
            command = 0
            # Continue to loop in the "command" variable is not in the list below
            while command not in ("lock", "l", "back", "b"):
                # Clear the console
                os.system("clear")
                # Show scanner commands
                print("-----------------------------------------------------------------\n")
                print("Scanner is ready\n")
                print("Type the command you would like to use\n")
                print("- (L)OCK - Use to lock a module to prevent aliens from escaping it")
                print("- (B)ACK - Go back to the action commands")
                # Ask the user for input
                command = input("> ")
                # Force the input to become lower cased
                command = command.lower()
            # If the input equals "lock" or "l"
            if command == "lock" or command == "l":
                # Stop the function and start the module locking process
                return lock()
            # If the input equals "back" or "b"
            elif command == "back" or command == "b":
                # Stop the function and re-load the module
                return reload_module()

# Spawn the npcs in random modules
def spawn_npcs():
    # Allow global variables to be changed
    global num_modules, queen, vent_shafts, info_panels, workers
    # Add all modules in an array except for the first module
    module_set = []
    for counter in range(2, num_modules + 1):
        module_set.append(counter)
    # Shuffle the modules
    shuffle(module_set)
    # Place the queen in the first module in the array
    i = 0
    queen = module_set[i]
    # Place the vent shafts in the 2nd, 3rd and 4th modules in the array
    for counter in range(3):
        i += 1
        vent_shafts.append(module_set[i])
    # Place the info panels in the 5th and 6th modules in the array
    for counter in range(2):
        i += 1
        info_panels.append(module_set[i])
    # Place the worker aliens in the 7th, 8th and 9th modules in the array
    for counter in range(3):
        i += 1
        workers.append(module_set[i])

# Check if the player is in a module that contains a vent shaft
def check_vent_shafts():
    # Allow global variable to be changed
    global num_modules, curr_module, last_module, vent_shafts, fuel
    # If the player is in a module that contains a vent shaft
    if curr_module in vent_shafts:
        # Start telling the player they entered a module with a vent shaft
        vent_shaft_message = "You walk into the room and you find some bank of fuel cells. You take one and load it into your flamethrower"
        for char in vent_shaft_message:
            print(char, end='')
            sys.stdout.flush()
            sleep(0.05)
        # Wait 2 seconds
        sleep(2)
        # Radomly select the number 20, 30, 40 or 50
        fuel_gained = randint(2, 5) * 10
        # Tell the player their old fuel reading and their new fuel reading
        print("Fuel was {0} now reading: {1}".format(fuel, fuel + fuel_gained))
        # Add the fuel to the player's fuel
        fuel += fuel_gained
        # Wait 2 seconds
        sleep(2)
        # Start the vent shaft door closure text
        vent_shaft_doors_shut = "The doors suddenly lock shut. You can't leave via the doors. What is happening to the station? Our only escape is to climb into the ventilation shaft which will take us to a random module on Charles Darwin."
        for char in vent_shaft_doors_shut:
            print(char, end='')
            sys.stdout.flush()
            sleep(0.05)
        # Wait 2 seconds
        sleep(2)
        # Tell the player they are moving to a new module
        print("We follow the passages and find outselves sliding down.")
        last_module = curr_module
        # Keep moving the player until they enter a module with no vent shafts
        while curr_module in vent_shafts or curr_module == last_module:
            curr_module = randint(1, num_modules)
        # Clear the console
        os.system("clear")
        # Stop the function and load the new module
        return load_module()

# Ask the player to lock a module
def lock():
    # Allow global variables to be changed
    global num_modules, power, locked
    # Ask the user for input
    new_lock = input("Enter module to lock: ")
    # If the input is not a number
    if new_lock.isnumeric == False:
        # Stop and re-call the function
        return lock()
    # Turn the input into a number
    new_lock = int(new_lock)
    # If the number is not a module number
    if new_lock < 0 or new_lock > num_modules:
        # Tell the player the operation failed
        print("Invalid module. Operation failed.")
    # If the number is the module the queen is in
    elif new_lock == queen:
        # Tell the player the operation failed
        print("Unable to lock module. Operation failed")
    # Or start to lock the module
    else:
        # Set the "locked" global variable to be the module the player inputted
        locked = new_lock
        # Tell the player the operation was successfull
        print("Aliens cannot get into module {0}. Power will be used. Operation sucessfull".format(locked))
    # Randomly generate amount of power to be drained
    power_used = 25 + 5 * randint(0, 5)
    # Remove power needed to be drained
    power -= power_used
    # If the power ran out
    if power <= 0:
        # Kill the player and stop the function
        alive == False
        return
    # Or stop the function
    else:
        return
    
# Calcuate the total damage applied to a player
def calculate_damage(damage):
    # If both damage reduction and increase are 0
    if damage_reduction == 0 and damage_increase == 0:
        # Stop the function and return the "damage" variable
        return damage
    # If the damage reduction is applied
    elif damage_reduction > 0:
        # Calculate the damage reduction
        baseDamage = floor((damage / damage_reduction) * 100)
        # Apply the defence if any
        totalDamage = baseDamage - defence
        # If the "totalDamage" is 0 or less
        if totalDamage <= 0:
            # Stop the function and return 0 to say no damage taken
            return 0
        # Or stop the function with the "totalDamage"
        else:
            return totalDamage
    # If the damage increase is applied
    elif damage_increase > 0:
        # Calculate the damage increase
        baseDamage = floor(damage * ((damage_increase / 100) + 1))
        # Apply the defence if any
        totalDamage = baseDamage - defence
        # On the rare ocation that "totalDamage" is 0 or less
        if totalDamage <= 0:
            # Stop the function and return 0 to say no damage taken
            return 0
        # Or stop the function with the "totalDamage"
        else:
            return totalDamage
    # Or if damage redcution or increase is a negative number for some reason
    else:
        # Stop the function and reder an error
        return render_error("DMGCAL", 'Calculation error while handling damage taken')

# Check if the queen is in the same module as the player
def move_queen():
    # Allow global variables to be changed
    global num_modules, curr_module, last_module, locked, queen, won, vent_shafts
    # If the player is in the queen's module
    if curr_module == queen:
        # Tell the player
        print("There it is! The queen alien in this module...")
        # Wait 5 seconds
        sleep(5)
        # Randomly give the queen chances to escape
        moves_to_make = randint(1, 3)
        # Stops the queen from moving to the last module
        can_move_to_last_module = False
        # While the queen has chances to escape, run the loop
        while moves_to_make > 0:
            # Get the connecting modules
            escapes = get_modules_from(queen)
            # Store the connecting modules correctly
            escapes = escapes[0]
            # If the current module is in the escapes array
            if curr_module in escapes:
                # Remove it
                escapes.remove(curr_module)
            # If the last module the player was in is in the escapes array
            if last_module in escapes and can_move_to_last_module == False:
                # Remove it
                escapes.remove(last_module)
            # If a locked module is in the escapes array
            if locked in escapes:
                # Remove it
                escapes.remove(locked)
            # If the queen has no modules to escape to
            if len(escapes) == 0:
                # The players wins and is told
                won = True
                moves_to_make = 0
                print("...and the door is locked. It's trapped")
            # Or if it does have an escape route
            else:
                # If it has 1 move to make
                if moves_to_make == 1:
                    # Let the queen escape
                    print("...and has escaped.")
                # Move the queen to a random module in the escapes array
                queen = choice(escapes)
                # Decrease the queen's moves to make by 1
                moves_to_make -= 1
                # Allow it to move to the last module if it placed connecting to it
                can_move_to_last_module = True
                # If the queen moves into a room with a vent shaft
                while queen in vent_shafts:
                    # If it has more than one move to make
                    if moves_to_make > 1:
                        # Let it escape
                        print("...and has escaped.")
                    # Tell the player the queen moved into a vent shaft
                    print("We can hear scuttling in the ventilation shafts.")
                    # Declare a variable to force the loop to start
                    valid_move = False
                    # While the "valid_move" variable is not True, loop
                    while valid_move != True:
                        # Set the "valid_move" to be True
                        valid_move = True
                        # Randomly move the queen to a module
                        queen = randint(1, num_modules)
                        # If the module is a vent shaft
                        if queen in vent_shafts:
                            # Set the "valid_move" to be False to continue the loop
                            valid_move = False
                    # Force the queen to have no more moves left
                    moves_to_make = 0

# Tell the player if something is nearby
def intuition():
    # Loop through the connecting modules
    for connected_module in possible_moves:
        # If one is a worker alien module
        if connected_module in workers:
            # Wait 1 second
            sleep(1)
            # Then tell the player
            print("I can hear something scuttling!")
        # If one is a vent shaft module
        if connected_module in vent_shafts:
            # Wait 1 second
            sleep(1)
            # Then tell the player
            print("I can feel cold air!")

# Check if the player is in the same module as a worker alien
def worker_aliens():
    # Allow global variables to be changed
    global workers, fuel, alive
    # If the player is in the same module as a worker alien
    if curr_module in workers:
        # Tell the player
        print("Startled, a young alien scuttles across the floor.")
        # Wait 1 second
        sleep(1)
        # Tell the player the alien noticed them
        print("It turns and leaps towards us.")
        # Delare a variable to force the loop to start
        successful_attack = False
        # While the "successful_attack" is not True
        while successful_attack != True:
            # Wait 1 second
            sleep(1)
            # Tell the player what they can do
            print("You can:\n")
            sleep(1)
            print("- Short blast your flamethrower to frighten it away.")
            print("- Long blast your flamethrower to try to kill it.\n")
            sleep(1)
            print("How will you react? (S, L)")
            # Delare a variable to force the loop to start
            action = 0
            # Whle the input is not in the list below
            while action not in ("s", "l"):
                # Ask the player for input
                action = input("Press the trigger: ")
                # Force the input to become lower cased
                action = action.lower()
            # Delare a variable to force the loop to start
            fuel_used = ""
            # While the input is not numeric
            while fuel_used.isnumeric() == False:
                # Ask the player for input
                fuel_used = input("How much fuel will you use? ...")
            # Turn the input into a number
            fuel_used = int(fuel_used)
            # Remove the fuel from the player's fuel
            fuel -= fuel_used
            # If the player has no fuel left
            if fuel <= 0:
                # Kill the player and stop the function
                alive = False
                return
            # If the "action" equals "s"
            if action == "s":
                # Randomly generate a required amount of fuel
                fuel_needed = 30 + 10 * randint(0, 5)
            # If the "action" equals "l"
            if action == "l":
                # Randomly generate a required amount of fuel
                fuel_needed = 90 + 10 * randint(0, 5)
            # If the fuel given is greater than or equal to the fuel needed
            if fuel_used >= fuel_needed:
                # Set the "successful_attack" to be True
                successful_attack = True
            # Or if it's not
            else:
                # Wait 1 second
                sleep(1)
                # Tell the player the attack was not successful
                print("The alien squeals but is not dead. It's angry")
        # Tell the player their attack was sucessful and remove the alien from the current module and stop the function
        if action == "s":
            sleep(1)
            print("The alien scuttles away into the corner of the room.")
        if action == "l":
            sleep(1)
            print("The alien has been destroyed.")
            workers.remove(curr_module)
        return print()

# Title Screen
show_title_screen()

# Main program starts here
os.system("clear")
# Spawn the npcs
spawn_npcs()

# Play the game while the player is alive and hasn't won
while alive and not won:
    # Call the correct functions
    load_module()
    check_vent_shafts()
    move_queen()
    worker_aliens()
    # If the player is still alive and hasn't won
    if won == False and alive == True and power > 0:
        # Continue playing
        intuition()
        sleep(1)
        output_moves()
        sleep(1)
        get_action()

# If the player won
if won == True:
    # Tell them
    sleep(1)
    print("The queen is trapped and you burn it to death with your flamethrower.")
    sleep(2)
    print("Game over. You win!")
# If the player is dead
if alive == False:
    # Tell them
    sleep(1)
    print("The station has ran out of power. Unable to sustain life support, you die.")
    sleep(2)
    print("Game over. You loose!")
