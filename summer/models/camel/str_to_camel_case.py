from typing import Set


def str_to_camel_case(_string: str) -> str:
    """
    Given string it returns a camel case version of it.
    """
    camel_cased_string: str = ""
    last_space = False
    space_set: Set[chr] = {" ", "_"}

    for i, c in enumerate(_string):
        if i == 0:
            camel_cased_string += str(c).lower()
        elif c in space_set:
            last_space = True
        elif last_space:
            last_space = False
            camel_cased_string += str(c).upper()
        else:
            camel_cased_string += str(c)

    return camel_cased_string
