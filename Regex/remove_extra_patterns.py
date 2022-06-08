import re
import sys


def remove_pattern(pattern: str, text: str) -> str:
    regex_to_remove_url = pattern
    removed_urls_text = re.sub(regex_to_remove_url, "", text)
    return removed_urls_text


def remove_urls(text: str) -> str:
    regex_to_remove_url = r"(https?):\/\/(www\.)?[a-z0-9\.:].*?(?=\s)"
    return remove_pattern(regex_to_remove_url, text)


def remove_phone_nums(text: str) -> str:
    regex_to_remove_phone = r"(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}"
    return remove_pattern(regex_to_remove_phone, text)


def remove_account_nums(text: str) -> str:
    regex_to_remove_account = r"(\d{4}[-]){3}\d{4}"
    return remove_pattern(regex_to_remove_account, text)


def remove_email(text: str) -> str:
    regex_to_remove_account = r"[a-zA-Z0-9]+@[a-z]+\.[A-Za-z]{2,3}"
    return remove_pattern(regex_to_remove_account, text)


def remove_extra_patterns(text_to_process: str) -> str:
    """
    Remove URLs, phone numbers, account id, and email.

    :param text_to_process: the text to process and to remove extra patterns in it.
    :return: processed text
    """
    processed_text = remove_urls(text_to_process)
    processed_text = remove_phone_nums(processed_text)
    processed_text = remove_account_nums(processed_text)
    processed_text = remove_email(processed_text)
    return processed_text


if __name__ == "__main__":
    """
    Command to run the code:
    python remove_extra_patterns.py input.txt cleaned_input.txt
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

    output = remove_extra_patterns(string_to_process)

    # writing to the output file with the given output path in the argv
    with open(output_path, "w") as f:
        f.write(output)
