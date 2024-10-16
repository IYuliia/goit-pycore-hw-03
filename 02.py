import random


def get_numbers_ticket(min, max, quantity):
    if min < 0 or max > 1000 or quantity > (max - min + 1) or quantity < 1:
        return []

    random_numbers = random.sample(range(min, max + 1), quantity)

    return sorted(random_numbers)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
