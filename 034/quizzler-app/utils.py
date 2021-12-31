import html

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
