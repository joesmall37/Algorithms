def win_percentage(wins, losses):
    total = wins + losses
    percentage = (wins / total) * 100
    return percentage


print(win_percentage(5, 5))
