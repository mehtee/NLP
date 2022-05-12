# Task 1
from typing import List
import re
import sys


def split(delimiters: List[str], string: str) -> List[str]:
    # Specifying multiple delimiters to split
    regexPattern = '|'.join(map(re.escape, delimiters))
    regexPattern = "(" + regexPattern + ")"
    return re.split(regexPattern, string)


def get_regex_set_of_punctuations(punctuations: tuple) -> str:
    # Given a list/tuple of punctuations, returns a regex pattern of the set of those punctuations
    punctuations_regex_pattern = "[" + ''.join(map(re.escape, punctuations)) + "]"
    return punctuations_regex_pattern


def remove_lines_without_punctuations(text_to_process: str) -> str:
    """
    This function gets a text to find and remove strings ending with "\n" and "\t" that is not ended with a Persian
    terminal punctuation
    :param text_to_process: the text to process and remove invalid strings.
    :return: processed text
    """

    # terminal punctuations of Farsi
    terminal_punctuations_tuple = "!", ".", "؛", "؟"
    punctuations_regex_pattern = get_regex_set_of_punctuations(terminal_punctuations_tuple)

    # list of delimiters to split the text
    delimiters = ["\n", "\t"]

    # Converting the given string to a list of splitted strings separated by "\n":
    splitted_string_list: List[str] = split(delimiters, text_to_process)
    # After processing each string ended by "\n" in the list, if it would be ended with a punctuation, we add to the
    # end of this string:
    after_processing_text: str = ""

    for i in range(len(splitted_string_list)):
        # If it ends with \W (which is any non-word character)
        # Alternatively we can use r'[^\w]$' (the negation of the set of \w which is \W) or a set of all of the punctuation marks.
        splitted_string = splitted_string_list[i]

        dilimeter_of_splitted_string = ""
        if (len(splitted_string_list) >= 1) and (i != 0):
            dilimeter_of_splitted_string = splitted_string_list[i - 1]

        if splitted_string not in delimiters:
            if re.search(punctuations_regex_pattern + r'$', splitted_string):
                after_processing_text += dilimeter_of_splitted_string + splitted_string

    return after_processing_text


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
