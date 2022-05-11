# Task 1
from typing import List
import re
import sys


def remove_lines_without_punctuations(text_to_process: str):
    """
    This function gets a text to find and remove strings ending with "\n" that is not ended with a punctuation (e.g !.)
    :param text_to_process: the text to process and remove invalid strings.
    :return: processed text
    """

    # Converting the given string to a list of splitted strings separated by "\n":
    splitted_string_list: List[str] = text_to_process.split("\n")
    # After processing each string ended by "\n" in the list, if it would be ended with a punctuation, we add to the
    # end of this string:
    after_processing_list: str = ""

    for split_string in splitted_string_list:
        # If it ends with \W (which is any non-word character)
        # Alternatively we can use r'[^\w]$' (the negation of the set of \w which is \W) or a set of all of the punctuation marks.
        if re.search(r'\W$', split_string):
            after_processing_list += split_string + "\n"

    return after_processing_list


if __name__ == "__main__":
    """
    Command to run the code:
    python remove_bad_lines.py input.txt cleaned_input.txt
    """
    string_to_process: str
    sys_args: list = sys.argv

    # If the args are not set properly, then exit
    if len(sys_args) != 3:
        exit()

    input_path: str = sys_args[1]
    output_path: str = sys_args[2]

    # reading the input file with the given input path in the argv
    with open(input_path, "r") as f:
        string_to_process = f.read()

    output = remove_lines_without_punctuations(string_to_process)

    # writing to the output file with the given output path in the argv
    with open(output_path, "w") as f:
        f.write(output)
