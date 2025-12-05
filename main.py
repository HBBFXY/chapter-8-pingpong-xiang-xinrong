import random

def print_intro():
    print("=" * 50)
    print("乒乓球竞技分析模拟程序")
    print("规则：每局11分制（需领先2分获胜），整场7局4胜制")
    print("参数：选手能力值（0-1之间的小数，代表单分获胜概率）")
    print("=" * 50)

def get_inputs():
    prob_a = float(input("请输入选手A的能力值(0-1): "))
    prob_b = float(input("请输入选手B的能力值(0-1): "))
    n_games = int(input("请输入模拟比赛的总场次: "))
    return prob_a, prob_b, n_games

def is_game_over(score_a, score_b):
    return (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2

def simulate_one_game(prob_a, prob_b):
    score_a, score_b = 0, 0
    serving = "A"
    while not is_game_over(score_a, score_b):
        if serving == "A":
            if random.random() < prob_a:
                score_a += 1
            else:
                serving = "B"
        else:
            if random.random() < prob_b:
                score_b += 1
            else:
                serving = "A"
    return score_a, score_b

def simulate_one_match(prob_a, prob_b):
    wins_a, wins_b = 0, 0
    for _ in range(7):
        score_a, score_b = simulate_one_game(prob_a, prob_b)
        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1
        if wins_a == 4 or wins_b == 4:
            break
    return wins_a, wins_b

def simulate_n_matches(n, prob_a, prob_b):
    total_wins_a, total_wins_b = 0, 0
    for _ in range(n):
        match_wins_a, match_wins_b = simulate_one_match(prob_a, prob_b)
        if match_wins_a > match_wins_b:
            total_wins_a += 1
        else:
            total_wins_b += 1
    return total_wins_a, total_wins_b

def print_summary(total_wins_a, total_wins_b, n):
    print("\n" + "=" * 50)
    print(f"模拟结果（共{ n }场比赛）")
    print(f"选手A获胜场次：{ total_wins_a }，胜率：{ total_wins_a / n * 100:.1f}%")
    print(f"选手B获胜场次：{ total_wins_b }，胜率：{ total_wins_b / n * 100:.1f}%")
    print("=" * 50)

def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    total_wins_a, total_wins_b = simulate_n_matches(n, prob_a, prob_b)
    print_summary(total_wins_a, total_wins_b, n)

if __name__ == "__main__":
    main()
