import sys
from PhotorazeController import Menu, CreateCommand, ReadCommand, UpdateCommand, DeleteCommand, SearchCommand
def main():
    menu = Menu()
    menu.add_command("create_view", CreateCommand(menu.receiver))
    menu.add_command("read_view", ReadCommand(menu.receiver))
    menu.add_command("update_view", UpdateCommand(menu.receiver))
    menu.add_command("delete_view", DeleteCommand(menu.receiver))
    menu.add_command("search_view", SearchCommand(menu.receiver))

    while True:
        print(sys.getrecursionlimit())
        print("Menu:")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Search")
        print("6. Exit")
        # template_renderer(context={}, template='default.jinja2', cls=cls)
        choice = input("Enter your choice: ")
        if choice == "6":
            break
        menu.execute_command(["create_view", "read_view", "update_view", "delete_view", "search_view"][int(choice) - 1])


if __name__ == "__main__":
    main()