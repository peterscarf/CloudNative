from database.jsonDAO import Database
from application.marketplace import Marketplace
import shlex

def main():
    db = Database(
    marketplace = Marketplace(db)
    
    while True:
        try:
            # command = input("# ").strip().split()
            command = shlex.split(input("# ").strip())
            if not command:
                continue

            action = command[0]

            if action == "REGISTER" and len(command) == 2:
                print(marketplace.register_user(command[1]))

            elif action == "CREATE_LISTING" and len(command) == 6:
                print(marketplace.create_listing(*command[1:]))

            elif action == "DELETE_LISTING" and len(command) == 3:
                print(marketplace.delete_listing(command[1], command[2]))

            elif action == "GET_LISTING" and len(command) == 3:
                print(marketplace.get_listing(command[1], command[2]))

            elif action == "GET_CATEGORY" and len(command) == 3:
                print(marketplace.get_category(command[1], command[2]))

            elif action == "GET_TOP_CATEGORY" and len(command) == 2:
                print(marketplace.get_top_category(command[1]))

            else:
                print("Error - invalid command")

        except EOFError:
            break

if __name__ == "__main__":
    main()
