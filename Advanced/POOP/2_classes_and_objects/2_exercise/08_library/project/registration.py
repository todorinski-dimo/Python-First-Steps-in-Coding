from project.library import Library
from project.user import User


class Registration:

    def __init__(self):
        pass

    @staticmethod
    def add_user(user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)
        return None

    @staticmethod
    def remove_user(user: User, library: Library):
        # if user.username in library.rented_books:
        #     del library.rented_books[user.username]
        if user in library.user_records:
            library.user_records.remove(user)
            return None
        return f"We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        found_user = next((u for u in library.user_records if u.user_id == user_id), None)
        if found_user:
            if new_username == found_user.username:
                return "Please check again the provided username - it should be different than the username used so far!"
            if found_user.username in library.rented_books:
                library.rented_books[new_username] = library.rented_books.pop(found_user.username)
            found_user.username = new_username
            return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"
