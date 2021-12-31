import html

def get_user_choice(input_prompt: str, valid_choices: list[str]):
    valid_input = False
    while not valid_input:
        user_input = input(input_prompt).lower()
        if user_input in valid_choices:
            valid_input = True
        else:
            pass
    return user_input

def unescape_html_in_dictionary(dictionary):
    if isinstance(dictionary, dict):
        for k, v in dictionary.items():
            if isinstance(v, dict):
                unescape_html_in_dictionary(k)
            elif isinstance(v, list):
                for list_item in v:
                    unescape_html_in_dictionary(list_item)
            elif isinstance(v, str):
                dictionary[k] = html.unescape(v)
            else:
                pass
        else:
            pass
