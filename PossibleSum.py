
import itertools
"""
from a given array of numbers, find the possible combinations to get input int
"""

# returns a list of tuples

def combo_list_maker(stuff):
    combo_list =[]
    for L in range(0, len(stuff)+1):
      for subset in itertools.combinations(stuff, L):
        combo_list.append(subset)
    return combo_list


def combo_finder(given_list, target_int):
    for tup in given_list:
        if sum(tup) == target_int:
            print(tup)


def combo(your_nums, target_int):
    combo_list = combo_list_maker(your_nums)
    combo_finder(combo_list, target_int)

my_nums = [6,6,6,6,7,7,11]
combo(my_nums, 40)

