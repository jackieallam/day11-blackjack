# ############## Blackjack Project #####################
import random
from art import logo
from os import system  # system("clear")

play_again = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
end_message = {
    "win_bj": "Win with a Blackjack 😎",
    "lose_bj": "Lose, opponent has Blackjack 😱",
    "win_over": "Opponent went over. You win 😁",
    "lose_over": "You went over. You lose 😭",
    "win": "You win 😃",
    "lose": "You lose 😤",
    "draw": "Draw 🙃",
}


def display_current_score():
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")


def display_final_score():
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")


def hit():
    yes = input("Type 'y' to get another card, type 'n' to pass: ")
    if yes == "y" or yes == "Y":
        player_cards.append(random.choice(cards))
        if (sum(player_cards) > 21) and (11 in player_cards):
            player_cards[player_cards.index(11)] = 1  # Replace 11 with 1
        display_current_score()
        if sum(player_cards) <= 21:
            hit()


def blackjack():
    # For testing:
    # player_cards.extend([11,2])  # For testing with specific cards
    # comp_cards.extend([11,5])
    player_cards.extend(random.sample(cards, 2))
    comp_cards.extend(random.sample(cards, 2))
    player_score = sum(player_cards)
    comp_score = sum(comp_cards) 
    display_current_score()
        
    if player_score <= 21:
        hit()

    while comp_score < 17:
        comp_cards.append(random.choice(cards))
        if 11 in comp_cards and sum(comp_cards) > 21:
            comp_cards[comp_cards.index(11)] = 1  # Replace 11 with 1
        comp_score = sum(comp_cards)

    player_score = sum(player_cards)
    display_final_score()

    if player_score > 21:
        end = end_message["lose_over"]
    elif comp_score > 21:
        end = end_message["win_over"]
    elif comp_score == 21:
        end = end_message["lose_bj"]
    elif player_score > comp_score:
        end = end_message["win"]
    elif comp_score > player_score:
        end = end_message["lose"]
    elif comp_score == player_score:
        end = end_message["draw"]
    if player_score == 21:
        if comp_score == 21:
            end = end_message["draw"]
        else:
            end = end_message["win_bj"]
    print(end)


while play_again:
    ask = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if ask == "n" or ask == "N":
        play_again = False
    elif ask == "y" or ask == "Y":
        system("clear")
        player_cards = []
        comp_cards = []
        print(logo)
        blackjack()
