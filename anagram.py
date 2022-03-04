'''
Write a code that checks if two given strings are anagrams

Sample Input: Mary Army

Output: Yes
'''


def check_anagram(input_str: str) -> str:
    """Checks if two strings are anagrams

    Args:
        input_str (str): _description_

    Returns:
        str: _description_
    """
    word_array = input_str.lower().split(' ')
    
    if len(word_array) == 0:
        return 'Yes'
    
    elif len(word_array) == 2:
    
        if sorted(word_array[0]) == sorted(word_array[1]):
            return 'Yes'
        
        else:
            return 'No'
    
    else:
        return 'No'
    

print(check_anagram('Mary Army'))
