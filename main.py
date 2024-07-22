from registration import register
from state_manager import StateManager
import os


class ExpenseTrackerApp:
    def __init__(self) -> None:
        self.state_manager = StateManager()

    def run(self):
        self.running = True
        os.system('cls')

        while self.running:
            self.state_manager.display_current_window()
            if input().lower() == 'q':
                self.running = False 

    def take_user_input():
        pass


if __name__ == '__main__':
    app = ExpenseTrackerApp() 
    app.run()