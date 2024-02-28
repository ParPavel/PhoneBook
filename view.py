import text

def show_main_menu() -> int:
    """

    :rtype: object
    """
    for i, item in enumerate(text.main_menu):
        if i:
            print(f'\t{i}. {item}')
        else:
            print(item)
    while True:
        choice = input(text.choice_main_menu)
        if choice.isdigit() and 0 < int(choice)< len(text.main.menu):
            return int(choice)
        print(text.choice_main_menu_error)



print(show_main_menu())