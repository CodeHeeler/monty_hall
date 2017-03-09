import random

def main():
    secret_win = 0
    first_pick = 0
    stay_wins = 0
    switch_wins = 0
    random_wins = 0
    stay_or_switch = 0

    num_games = int(input("How many games of each strategy? "))
    for i in range(num_games):
        secret_win = random.randint(1, 3)
        first_pick = random.randint(1, 3)
        if secret_win == first_pick:
            stay_wins += 1
    for i in range(num_games):
        secet_win = random.randint(1, 3)
        first_pick = random.randint(1, 3)
        if secret_win != first_pick:
            switch_wins += 1
    for i in range(num_games):
        secret_win = random.randint(1, 3)
        first_pick = random.randint(1, 3)
        stay_or_switch = random.randint(0, 1)
        if secret_win != first_pick:
            if stay_or_switch:
                random_wins += 1
        else:
            if not stay_or_switch:
                random_wins += 1

    print("Times always staying won: {}".format(stay_wins))
    print("Times always switching won: {}".format(switch_wins))
    print("Times a random strategy won: {}".format(random_wins))


if __name__ == "__main__":
    main()
