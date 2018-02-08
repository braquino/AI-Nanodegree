import random

def draw_chance(cards_drawn=1, total_cards=52):

    chance = (1.0 / total_cards)
    total_cards -= 1
    for i in range(cards_drawn-1):
        not_draw = (1 - chance)
        chance += not_draw * (1.0 / total_cards)
        total_cards -= 1
    return chance

def sum_chances(*chances):
    current_chance = 0
    for chance in chances:
        not_chance = 1 - current_chance
        current_chance += not_chance * chance
    return current_chance


print(draw_chance(2))
print(sum_chances(draw_chance(5), draw_chance(5)))

list(zip(lambda x,y : x in y, [1, 2], [3, 4, 2, 1]))
