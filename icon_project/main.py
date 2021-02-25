"""
creator:Leon Boczkowski
class: Python 2
project: icons
"""


# imports

def user_input():
    """
    Requires user to input digits of 0 or ones and adds those digits to a list. A total of 10 lists
    of 10 digits is stores in a list of lists. that list of lists is then passed nested lists
    :return:list of lists. Returns 10 lists of inputted digits
    """
    # to store 10s and z
    digit_list = []
    list_of_lists = []

    count = 0
    for outer in range(2):

        # appends digit list to lists of lists after appending 10 digits to digit list.
        list_of_lists.append([])

        for inner in range(10):

            try:
                # asks users for input and add input to digit_list.
                ui = input(f'Please enter either a zero or 1.')

            # runs if non number value entered.
            except (ValueError, TypeError) as e:

                print("WARNING!")
                print(e)
                print("Did not enter 0 or 1.")

                # asks users for input and add input to digit_list.
                ui = input(f'Please enter either a zero or 1.')

            finally:
                # #runs if the digit length is greater than 2.
                if len(ui) >= 2:
                    # reduces ui to 1 digit only.
                    ui = ui[0]

                # assigns a 0 to any digit entered not a 0 or 1.
                if not ui != "0" or ui != "1":
                    ui = 0

                # appends digits to list.
                list_of_lists[outer].append(f'{ui}')

            count += 1

        # outputs quantity of digits entered.
        print(f'\nYou have completed {count} of entering 100 digits!\n\n')

    return list_of_lists


def output(list_of_lists):
    """
    Takes list/lists loops through and changes digits to special characters and then outputs results.
    :param list_of_lists: takes list of lists as param.
    :return: returns list of lists containing digits.
    """

    # for inner_list in list_of_lists:
    for row in list_of_lists:

        # loops through inner list.
        for icon in row:
            # replaces each digits as space or star.
            icon = icon.replace("0", " ").replace("1", "*")

            # outputs graphics inline
            print(f' {icon}', end="")

        # moves to next line for next list to be outputted.
        print()


def inverted_output(list_of_lists):
    """
    Takes list/lists loops through and changes digits to special characters and then outputs results inverted style.
    :param list_of_lists: takes list of lists as param.
    :return: returns list of lists containing digits.
    """

    # for inner_list in list_of_lists:
    for row in list_of_lists:

        # loops through inner list.
        for icon in row[::-1]:
            # replaces each digits as space or star.
            icon = icon.replace("0", " ").replace("1", "*")

            # outputs graphics inline
            print(f' {icon}', end="")

        # moves to next line for next list to be outputted.
        print()


def output_menu_options(list_of_lists):
    """
    Function presents user a menu of options and functions to run on that option. Once user has decided it will run 1 of
    the following functions:
    inverted_output(list_of_lists)
    output(list_of_lists)
    :param list_of_lists: returned from us user_input() function.
    :return: nothing
    """

    # creates  list of options to run on user commands.
    func_option_list = ["output", "invert output"]

    # creates  list of functions to run on user commands.
    funcs_run_list = [output, inverted_output]

    # loops through user options.
    for num, fun in enumerate(func_option_list, 1):
        print(f'{num}:\t{fun}')

    try:
        # request user to decide command to run from list.
        ui = int(input("\nEnter the number of the command you would like to run: "))

        print('\n')
        # runs if non number value entered.

    except (ValueError, TypeError) as e:

        print("WARNING!")
        print(e)
        print("Did not enter 0 or 1.")

        # asks users for input and add input to digit_list.
        ui = input(f'Please enter either a zero or 1.')
    # Runs command user picked.
    funcs_run_list[ui - 1](list_of_lists)


# _________________________________________________________________________________#
# main
if __name__ == '__main__':
    # holds inputted digits list.
    list_of_digits_list = []
    # defines and outputs user task.
    print("This program will take 0 or 1 as an input and output a graphic that you have decided.\nEnter either a 0 or 1"
          " x 10 times. it will then ask you to input another 10 characters, up to 100 characters in total.")

    # Takes lists of digits and turns into characters.
    list_of_lists = user_input()

    # takes list_of_list and returns printed graphic.
    output_menu_options(list_of_lists)
