"""
Write a code that prints out individual scores of two players in a game of 
cricket where score is given as runs per ball in an array. In a game of 
cricket a person changes strike if he scores an odd number, and keeps strike 
with him if he scores an even number. No need to consider changing strike
after every 6 balls or an over.

Sample Input1: [1,2]

Output1: p1: 1, p2: 2

Sample Input2: [1,2,3,2,1]

Output2: p1: 4, p2: 5
"""


def cricket_score(runs_array: list) -> str:
    """This returns the individual scores of two players

    Args:
        runs_array (list): _description_

    Returns:
        str: _description_
    """
    p1_score = 0
    p2_score = 0

    is_p1_active = True

    for run in runs_array:

        if is_p1_active:
            p1_score += run

        else:
            p2_score += run

        if run % 2 != 0:
            is_p1_active = not is_p1_active

    return f"p1: {p1_score}, p2: {p2_score}"


print(cricket_score([1, 2, 3, 2, 1]))
