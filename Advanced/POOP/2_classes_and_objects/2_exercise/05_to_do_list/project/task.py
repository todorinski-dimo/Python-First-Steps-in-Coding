class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: list = []
        self.completed: bool = False

    def change_name(self, new_name: str) -> None | str:
        if self.name == new_name:
            return "Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_due_date: str) -> None | str:
        if self.due_date == new_due_date:
            return "Date cannot be the same."
        self.due_date = new_due_date
        return self.due_date

    def add_comment(self, new_comment: str) -> None:
        self.comments.append(new_comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> None | str:
        if 0 <= comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ", ".join(self.comments)
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"