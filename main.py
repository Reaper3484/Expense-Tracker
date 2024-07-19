from registration import register


def display_menu():
    print('1: Show Budget')
    print('2: Register New User')
    print('3: Login')
    print("4: Show Budget")
    print("5: Allocate Budget")
    print("6: Add Expense")
    print("7: Settings")
    print("8: Show report")
    print("9: Add Income Source")
    print("10: Recurring Expense")
    print("11: Filter")
    print("12: User Profile and authentication")
    print("q: Quit")


def take_user_input():
    user_input = input().lower()
    return user_input


running = True
while running:
    display_menu()
    if take_user_input() == 'q':
        running = False
