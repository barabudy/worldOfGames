def welcome(name):
    return "Hello %s and welcome to the World of Games (WoG).\nHere you can find many cool games to play." % name


def load_game():
    chosen_game_name = None
    user_game_choice = int(
        input("\nPlease choose a game to play:\n\t1.Memory Game - a sequence of numbers will appear for "
              "1 second and you have to guess it back\n\t2.Guessing Game - guess a number and see if you "
              "chose like the computer\n\t""3.Currency Roulette - try and guess the value of a random "
              "amount of USD in ILS\n"))

    while user_game_choice != 1 and user_game_choice != 2 and user_game_choice != 3:
        print("\nPlease choose any of the following:")
        user_game_choice = int(input("\t1.Memory Game\n\t2.Guessing Game\n\t3.Currency Roulette\n"))

    if user_game_choice == 1:
        chosen_game_name = "Memory Game"
    elif user_game_choice == 2:
        chosen_game_name = "Guessing Game"
    else:
        chosen_game_name = "Currency Roulette"

    choose_difficulty(user_game_choice, chosen_game_name)


def choose_difficulty(p_chosen_game, p_game_name):
    game_level = int(input("\nTo play %s please choose a difficulty level from 1 to 5\n" % p_game_name))
    while game_level < 1 or game_level > 5:
        game_level = int(input("Invalid choice. Please choose a level from 1 to 5\n"))
    print("You chose level %d" % game_level)


