# 2022 Day 1 advent calendar

calories = './input.txt'

file1 = open(calories, 'r')
lines = file1.readlines()


def separate_reindeer():
    reindeer = {}
    number_of_rein = 1
    for line in lines:
        stripped_line = line.strip()
        if len(stripped_line) == 0:
            number_of_rein += 1
        else:
            if f'rein_{number_of_rein}' in reindeer:
                reindeer[f'rein_{number_of_rein}'] += int(stripped_line)
            else:
                reindeer.update({f'rein_{number_of_rein}': int(stripped_line)})

    return reindeer


# Part 2
def first_three(sorted_dict):
    total_cal = 0
    for rein, calorie in sorted_dict:
        total_cal += calorie
    return total_cal


def main():
    sorted_dict = sorted(separate_reindeer().items(), key=lambda item: item[1], reverse=True)
    # Part 1
    print('The deer with the most calories', sorted_dict[1])
    # Part 2
    print('sum of calories for 3 deer', first_three(sorted_dict[:3]))


main()
