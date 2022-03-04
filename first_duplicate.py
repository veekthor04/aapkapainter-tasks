"""
Write a code that prints out the first occurrence of a duplicate in a given array of integers

Sample Input: [1,2,3,2,1]

Output: 2
"""


def first_duplicate(int_array: list) -> int:
    """Returns the first occurrence of a duplicate in an array

    Args:
        int_list (list): _description_

    Returns:
        int: _description_
    """

    ref_dict = {}

    for current_int in int_array:

        if ref_dict.get(current_int) != None:
            return current_int
        else:
            ref_dict[current_int] = 1
    return None


print(first_duplicate([1, 2, 3, 4, 5, 6, 7, 2, 1]))
