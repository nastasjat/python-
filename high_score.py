# save the highest scores to a new csv file
import csv


def read_from_file(file_name):
    text = []
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            text.append((row[0], int(row[1])))

    return text


def get_highest_scores(scores):
    highest = {}
    for player, score in scores:
        if player not in highest or score > highest[player]:
            highest[player] = score

    sorted_highest = sorted(highest.items(), key=lambda x: x[1], reverse=True)

    return sorted_highest


def save_to_file(highest_results, file_name):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player name", "Highest score"])
        writer.writerows(highest_results)


text = read_from_file("game_scores.csv")
results = get_highest_scores(text)
save_to_file(results, "highest_scores.csv")
