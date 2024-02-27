import json
import random
import time
import requests
from enum import Enum
from Player import Player


class Mode(Enum):
    COMP = 1
    PLAYER = 2
    GAME = 3
    STATS = 4


users = []


# Time decorator
def timeit(method):
    def timed(*args, **kw):
        start_time = time.time()
        result = method(*args, **kw)
        end_time = time.time()

        print(f"{method.__name__} took {end_time - start_time:.3f} seconds to execute")
        return result

    return timed


# Vergleich der Regeln
def get_winner(choice1, choice2):
    rules = {
        "Scissors": ["Paper", "Lizard"],
        "Paper": ["Rock", "Spock"],
        "Rock": ["Lizard", "Scissors"],
        "Lizard": ["Spock", "Paper"],
        "Spock": ["Scissors", "Rock"]
    }
    if choice2 in rules[choice1]:
        return 1
    elif choice1 in rules[choice2]:
        return 2
    else:
        return 0


@timeit
def player_choice(player_number):
    choices = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]
    print(f"Player {player_number}, enter your choice:")
    for idx, choice in enumerate(choices, 1):
        print(f"{idx}. {choice}")
    choice = int(input()) - 1
    return choices[choice]


def computer_choice():
    return random.choice(["Rock", "Paper", "Scissors", "Spock", "Lizard"])


def loadUsersToStats():
    try:
        with open('stats.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File does not exists")


def saveUserToUsers(user):
    for usr in users:
        if usr["nickname"] == user.nickname:
            usr["wins"] += user.wins
            usr["loses"] += user.loses
            usr["ties"] += user.ties
            break
    else:
        users.append(user.__dict__)


def saveUsersToFile():
    with open('stats.json', 'w') as file:
        json.dump(users, file, indent=2)


@timeit
def play_game():
    print("Welcome to Rock-Paper-Scissors-Spock-Lizard Game!")
    choice = int(input("Do you want to play [3] or see the statistics [4]:\n"))
    if choice == Mode.GAME.value:
        print("Enter your nickname: ")
        player_one.nickname = str(input())
        print("Choose your mode:\n1. COMP (play against the computer)\n2. PLAYER (play against another player)")
        mode = int(input())

        while True:
            if mode == Mode.COMP.value:
                while True:
                    player1_choice = player_choice(1)
                    update_stats(player_one, player1_choice)
                    computer = computer_choice()
                    print(f"Computer chose: {computer}")
                    winner = get_winner(player1_choice, computer)
                    if winner == 1:
                        print(f"{player_one.nickname} wins!")
                        player_one.wins += 1
                    elif winner == 2:
                        player_one.loses += 1
                        print("Computer wins!")
                    else:
                        print("It's a tie!")
                    user_input = input("Do you want to continue (yes/no): \n")
                    player_one.ties += 1
                    if user_input.lower() != "yes":
                        break
            elif mode == Mode.PLAYER.value:
                player_two.nickname = input("[PLAYER 2] Enter your nickname: \n")
                while True:
                    player1_choice = player_choice(1)
                    update_stats(player_one, player1_choice)
                    player2_choice = player_choice(2)
                    update_stats(player_two, player2_choice)
                    winner = get_winner(player1_choice, player2_choice)
                    if winner == 1:
                        player_one.wins += 1
                        player_two.loses += 1
                        print(f"{player_two.nickname} wins!")
                    elif winner == 2:
                        player_one.loses += 1
                        player_two.wins += 1
                        print(f"{player_two.nickname} wins!")
                    else:
                        print("It's a tie!")
                    user_input = input(f"Continue playing against {player_two.nickname}\n")
                    if user_input.lower() != "yes":
                        break
            else:
                print("Invalid mode selected.")

            user_input = input("Do you want to change the game mode? (yes/no): \n")
            if user_input.lower() != "yes":
                saveUserToUsers(player_one)
                insert_new_entry(player_one)
                if player_two.nickname != "":
                    saveUserToUsers(player_two)
                    insert_new_entry(player_two)
                break
    elif choice == Mode.STATS.value:
        print("JSON: Statistics:")
        sorted_users = sorted(users, key=lambda x: x['wins'], reverse=True)

        for user in sorted_users:
            print(f"Nickname: {user['nickname']}")
            print(f"Wins: {user['wins']}")
            print(f"Loses: {user['loses']}")
            print(f"Ties: {user['ties']}")
            print("-" * 20)

        print()
        print("DATABASE: Statistics")
        get_entries()


# Zusatz
def update_stats(player, choice):
    if choice == "Scissors":
        player.scissors += 1
    elif choice == "Rock":
        player.rock += 1
    elif choice == "Paper":
        player.paper += 1
    elif choice == "Spock":
        player.spock += 1
    elif choice == "Lizard":
        player.lizard += 1


def insert_new_entry(player):
    url = "http://127.0.0.1:5000/saveStat"
    query = {
        'nickname': player.nickname,
        'rock': player.rock,
        'paper': player.paper,
        'scissors': player.scissors,
        'spock': player.spock,
        'lizard': player.lizard
    }
    res = requests.post(url, json=query)
    print(res.text)


def get_entries():
    url = "http://127.0.0.1:5000/getStats"
    res = requests.get(url)
    data = res.json()

    if 'stats' in data:
        for row in data['stats']:
            print(row)
    else:
        print("No statistics available")


if __name__ == '__main__':
    player_one = Player("", 0, 0, 0, 0, 0, 0, 0, 0)
    player_two = Player("", 0, 0, 0, 0, 0, 0, 0, 0)
    users = loadUsersToStats()

    play_game()
    saveUsersToFile()
