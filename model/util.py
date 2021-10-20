import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_specialchars=r"+-!"):

    small_letters = list(string.ascii_letters.lower())
    capital_letters = list(string.ascii_letters.upper())
    digits = list(string.digits)
    special_characters = list(allowed_specialchars)
    id_number = []

    for i in range(number_of_small_letters):
        id_number.append(random.choice(small_letters))

    for i in range(number_of_capital_letters):
        id_number.append(random.choice(capital_letters))

    for i in range(number_of_digits):
        id_number.append(random.choice(digits))

    for i in range(number_of_special_chars):
        id_number.append(random.choice(special_characters))

    random.shuffle(id_number)

    return "".join(id_number)