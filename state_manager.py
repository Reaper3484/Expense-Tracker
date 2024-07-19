class AppState():
    MAIN_MENU = 0
    REGISTERATION = 1
    LOGIN = 2
    SHOW_BUDGET = 3
    ADD_EXPENSE = 4
    SETTINGS = 5
    SHOW_REPORT = 6
    ADD_INCOME_SOURCE = 7
    RECURRING_EXPENSE = 8
    SEARCH = 9
    QUIT = 10


class StateManager():
    def __init__(self) -> None:
        self.state = AppState.MAIN_MENU

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state
