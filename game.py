# simulate a game and save results to a csv file
import csv
import random


def simulate_game():
    players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
    scores = []

    for player in range(100):
        for player in players:
            score = random.randint(0, 1000)
            scores.append((player, score))

    return scores


def save_to_file(scores, file_name):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player name", "Score"])
        writer.writerows(scores)


game = simulate_game()
save_to_file(game, "game_scores.csv")
