import todoist
from todoist.models import Item
api_key = "fb962ee60a310b9434ceeb65af632e8989bd9a94"
user_account = todoist.TodoistAPI(api_key)

def main():
    flag = True
    ADD = 1
    REMOVE = 2
    QUIT = 0
    user_choice = int(input("What would you like to do?\n"
                            "1)\t Add A Focus Todo\n"
                            "2)\t Remove a Focus Todo\n"
                            "0)\t Quit"))
    while flag:
        if user_choice == ADD:
            user_todo = input("What would you like to do?")
            user_account.add_item(user_todo)
        elif user_choice == REMOVE:
            user_todo = input("What Focus todo would you like to remove?")
            items = todoist.models.Item(user_todo, user_account)
            items.complete()


if __name__ == '__main__':
    main()