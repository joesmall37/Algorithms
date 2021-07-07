# hide card number


# def hide_card(card_number):
#     # first two chars
#     return card_number[:2]

# my_card = hide_card('1111111')
# print(my_card)


def hide_card(card_number):
    cards_list = []
    last_four_digits = card_number[-4:]
    formatted_credit_card = "**** **** **** ", last_four_digits
    cards_list.append(formatted_credit_card)


    return cards_list


my_card = hide_card(['123456789111111'])

print(my_card)
