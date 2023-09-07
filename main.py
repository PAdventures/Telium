# Importing useful packages

from time import *  # To use the sleep() procedure to make the program run smoother
from random import *  # Use for randomising certain things such as chances
import os  # Useage for using commands in the terminal
import sys  # Exiting the program

# Global Variables

num_modules = 20  # The number of modules in the Charles Darwin
curr_module = 1  # The number of the current module that the player is in
last_module = 0  # The number of the last module the player was in
possible_moves = []  # The modules that the player can move to
curr_deck = ""  # The letter of the deck the player is in
curr_room = ""  # The module description of the player's current module
alive = True  # Is the player alive
won = False  # Has the player won
hp = 100  # Player health
defence = 10  # Player defence
power = 100  # The amount of power the space station has
fuel = 500  # The amount of fuel the player has to use their flamethrower
locked = 0  # The module that is locked by the player
queen = 0  # The module that the alien queen is in
vent_shafts = []  # The modules where vent shafts are located in
info_panels = []  # The modules where information panels are located in
workers = []  # The modules where alien workers are located in

# Procedure declarations

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
        sleep(0.1)
    sleep(5)

    print("")
    for char in paragraph2:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.1)
    sleep(8)

    print("")
    for char in paragraph3:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.1)
    sleep(5)

    print("")
    for char in paragraph4:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.1)
    sleep(10)

    print("")
    for char in paragraph5:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.1)
    sleep(8)

    print("")
    for char in paragraph6:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.2)
    sleep(5)

    print("")
    for char in paragraph7:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.1)
    sleep(5)

    print("")
    for char in paragraph8:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.2)
    sleep(5)

    print("")
    for char in paragraph9:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.1)
    sleep(5)
    os.system('clear')

def render_error(custom_code, message, timeout = 5):
    while timeout != -1:
        os.system('clear')
        print("-----------------------------------------------------------------")
        print("Error: {0}".format(custom_code))
        print("Message: {0}".format(message))
        print("-----------------------------------------------------------------")
        print("Stopping game in {0} seconds".format(timeout))
        timeout -= 1
        sleep(1)
    os.system('clear')
    sys.exit()

def handle_help_text_file_rendering(type="", code=""):
    if type != "query":
        return render_error("TYPENOTFOUND", "Param \"type\" given in help text file rendering does not exist", 5)
    text_file = open("Help_Text/{0}_{1}.txt".format(type, code), 'r')
    os.system('clear')
    print(text_file.read())
    print("\n")
    print("-----------------------------------------------------------------")
    option = input("(R)eturn to help menu: ")
    if option == "R" or option == "r":
        return display_help()
    else:
        return handle_help_text_file_rendering(type, code)
    

def display_instructions():
    os.system('clear')
    print("1. To win you must find and kill the Alien Queen, Telium, by blocking all of it's exits and killing it with your flamethrower")
    print("2. You can use the commands M(2) or MOVE(2) to move to a connecting module next to your current module")
    print("3. Alien workers are placed randomly around the station and can cause you trouble")
    print("4. Ventilation shafts will randomly move around the station")
    print("5. You can lock 1 module at a time to block the aliens")
    print("6. If you run out of health or the staion runs out of power you die")
    option = input("(R)eturn to menu: ")
    if option == "R" or option == "r":
        return show_title_screen()
    else:
        return display_instructions()

def display_help():
    option = 0
    while option not in ("aq", "wa", "vs", "ip", "lm", "mc", "ss", "ps", "r"):
        os.system('clear')
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
        option = input("> ")
        option = option.lower()
    if option == "r":
        return show_title_screen()
    return handle_help_text_file_rendering("query", option)


def show_title_screen():
    option = 0
    while option not in ("play", "p", "story", "s", "help", "h", "instructions", "i", "quit", "q"):
        os.system("clear")
        print("-----------------------------------------------------------------")
        print("Play (P)\nStory (S) - Recommended\nHelp (H) - Ask a query on a game machanic\nInstructions (I) - How to play\nQuit (Q)")
        print("-----------------------------------------------------------------\n")
        print("Type the option you would like to select")
        option = input("> ")
        option = option.lower()
    if option == "play" or option == "p":
        return
    elif option == "story" or option == "s":
        display_story()
        show_title_screen()
    elif option == "help" or option == "h":
        display_help()
    elif option == "instructions" or option == "i":
        display_instructions()
    elif option == "quit" or option == "q":
        os.system("clear")
        sys.exit()
    else:
        os.system("clear")
        sys.exit()


def load_module():
    global curr_module, possible_moves, curr_deck, curr_room
    module = get_modules_from(curr_module)
    possible_moves = module[0]
    curr_deck = module[1]
    curr_room = module[2]
    output_module()


def get_modules_from(module):
    moves = []
    deck = ""
    room = ""
    text_file = open("Charles_Darwin/module" + str(module) + ".txt", "r")
    for counter in range(0, 6):
        move_read = text_file.readline()
        if counter == 4:
            deck = move_read.strip()
        elif counter == 5:
            room = move_read.strip()
        else:
            move_read = int(move_read.strip())
            if move_read != 0:
                moves.append(move_read)
    text_file.close()
    return moves, deck, room


def start_story_line():
    os.system("clear")


def reload_module():
    os.system('clear')
    output_module()
    move_queen()
    output_moves()
    get_action()


def output_module():
    os.system('clear')
    global curr_module
    print("-----------------------------------------------------------------\n")
    print(curr_deck + " >>> " + curr_room)
    print()
    print("You are in module", curr_module)
    print("\n-----------------------------------------------------------------\n")


def output_moves():
    global possible_moves
    print("\nFrom here you can move to modules: | ", end=' ')
    for move in possible_moves:
        print(move, ' | ', end=' ')
    print()


def get_action():
    global curr_module, last_module, possible_moves, power
    valid_action = False
    while valid_action == False:
        print("What do you want to do next ?")
        print("\n- (M)OVE - Optional syntax include module number moving to || Example: M2 or MOVE2")
        print("- (S)CANNER")
        action = input("> ")
        action = action.upper()
        sleep(1)
        if action.find("M") == 0:
            if len(action) == 1 or len(action) == 4:
                print("Enter the module to move to or go back to the actions || Example: 2 or B or BACK")
                move = input("> ")
                move = move.lower()
            if len(action) == 2:
                actionArray = list(action)
                if (actionArray[1].isdigit()):
                    move = int(actionArray[1])
            if len(action) == 5:
                actionArray = list(action)
                if (actionArray[1].isdigit()):
                    move = int(actionArray[4])
            if move == "back" or move == "b":
                return reload_module()
            elif move.isnumeric() == False:
                return reload_module()
            elif int(move) in possible_moves:
                valid_action = True
                last_module = curr_module
                curr_module = move
                power -= 1
                if power <= 0:
                    alive == False
                    return
            else:
                sleep(1)
                print("The module must be connected to the current module.")
                sleep(3)
                return reload_module()
        if action.find("S") == 0:
            command = 0
            while command not in ("lock", "l", "back", "b"):
                os.system("clear")
                print(
                    "-----------------------------------------------------------------\n")
                print("Scanner is ready\n")
                print("Type the command you would like to use\n")
                print("- (L)OCK - Use to lock a module to prevent aliens from escaping it")
                print("- (B)ACK - Go back to the action commands")
                command = input("> ")
                command = command.lower()
            if command == "lock" or command == "l":
                lock()
            elif command == "back" or command == "b":
                return reload_module()


def spawn_npcs():
    global num_modules, queen, vent_shafts, info_panels, workers
    module_set = []
    for counter in range(2, num_modules + 1):
        module_set.append(counter)
    shuffle(module_set)
    i = 0
    queen = module_set[i]
    for counter in range(3):
        i += 1
        vent_shafts.append(module_set[i])

    for counter in range(2):
        i += 1
        info_panels.append(module_set[i])

    for counter in range(3):
        i += 1
        workers.append(module_set[i])


def check_vent_shafts():
    global num_modules, curr_module, last_module, vent_shafts, fuel
    if curr_module in vent_shafts:
        vent_shaft_message = "You walk into the room and you find some bank of fuel cells. You take one and load it into your flamethrower"
        for char in vent_shaft_message:
            print(char, end='')
            sys.stdout.flush()
            sleep(0.05)
        sleep(2)
        fuel_gained = randint(2, 5) * 10
        print("Fuel was {0} now reading: {1}".format(fuel, fuel + fuel_gained))
        fuel += fuel_gained
        sleep(2)
        vent_shaft_doors_shut = "The doors suddenly lock shut. You can't leave via the doors. What is happening to the station? Our only escape is to climb into the ventilation shaft which will take us to a random module on Charles Darwin."
        for char in vent_shaft_doors_shut:
            print(char, end='')
            sys.stdout.flush()
            sleep(0.05)
        sleep(2)
        print("We follow the passages and find outselves sliding down.")
        last_module = curr_module
        while curr_module in vent_shafts or curr_module == last_module:
            curr_module = randint(1, num_modules)
        os.system("clear")
        load_module()


def lock():
    global num_modules, power, locked
    new_lock = int(input("Enter module to lock: "))
    if new_lock < 0 or new_lock > num_modules:
        print("Invalid module. Operation failed.")
    elif new_lock == queen:
        print("Operation failed. Unable to lock module.")
    else:
        locked = new_lock
        print("Aliens cannot get into module {0}".format(locked))
    power_used = 25 + 5 * randint(0, 5)
    power -= power_used
    if power <= 0:
        alive == False
        return


def move_queen():
    global num_modules, curr_module, last_module, locked, queen, won, vent_shafts
    if curr_module == queen:
        print("There it is! The queen alien in this module...")
        sleep(5)
        moves_to_make = randint(1, 3)
        can_move_to_last_module = False
        while moves_to_make > 0:
            escapes = get_modules_from(queen)
            if curr_module in escapes:
                escapes.remove(curr_module)
            if last_module in escapes and can_move_to_last_module == False:
                escapes.remove(last_module)
            if locked in escapes:
                escapes.remove(locked)
            if len(escapes) == 0:
                won = True
                moves_to_make = 0
                print("...and the door is locked. It's trapped")
            else:
                if moves_to_make == 1:
                    print("...and has escaped.")
                queen = choice(escapes)
                moves_to_make -= 1
                can_move_to_last_module = True
                while queen in vent_shafts:
                    if moves_to_make > 1:
                        print("...and has escaped.")
                    print("We can hear scuttling in the ventilation shafts.")
                    valid_move = False
                    while valid_move == False:
                        valid_move = True
                        queen = randint(1, num_modules)
                        if queen in vent_shafts:
                            valid_move = False
                    moves_to_make = 0


def intuition():
    global possible_moves, workers, vent_shafts
    for connected_module in possible_moves:
        if connected_module in workers:
            sleep(1)
            print("I can hear something scuttling!")
        if connected_module in vent_shafts:
            sleep(1)
            print("I can feel cold air!")


def worker_aliens():
    global curr_module, workers, fuel, alive
    if curr_module in workers:
        print("Startled, a young alien scuttles across the floor.")
        sleep(1)
        print("It turns and leaps towards us.")
        successful_attack = False
        while successful_attack == False:
            sleep(1)
            print("You can:\n")
            sleep(1)
            print("- Short blast your flamethrower to frighten it away.")
            print("- Long blast your flamethrower to try to kill it.\n")
            sleep(1)
            print("How will you react? (S, L)")
            action = 0
            while action not in ("S", "L"):
                action = input("Press the trigger: ")
            fuel_used = int(input("How much fuel will you use? ..."))
            fuel -= fuel_used
            if fuel <= 0:
                alive = False
                return
            if action == "S":
                fuel_needed = 30 + 10 * randint(0, 5)
            if action == "L":
                fuel_needed = 90 + 10 * randint(0, 5)
            if fuel_used >= fuel_needed:
                successful_attack = True
            else:
                sleep(1)
                print("The alien squeals but is not dead. It's angry")
        if action == "S":
            sleep(1)
            print("The alien scuttles away into the corner of the room.")
        if action == "L":
            sleep(1)
            print("The alien has been destroyed.")
            workers.remove(curr_module)
        print()


# Title Screen
show_title_screen()

# Main program starts here
os.system("clear")
spawn_npcs()

# Developer tool
print("Queen alien is located in module:", queen)
print("Ventilation shatfs are located in modules:", vent_shafts)
print("Information panels are located in modules:", info_panels)
print("Alien workers are located in modules:", workers)

while alive and not won:
    load_module()
    check_vent_shafts()
    move_queen()
    worker_aliens()
    if won == False and alive == True and power > 0:
        intuition()
        sleep(1)
        output_moves()
        sleep(1)
        get_action()

if won == True:
    sleep(1)
    print("The queen is trapped and you burn it to death with your flamethrower.")
    sleep(2)
    print("Game over. You win!")
if alive == False:
    sleep(1)
    print("The station has ran out of power. Unable to sustain life support, you die.")
    sleep(2)
    print("Game over. You loose!")
