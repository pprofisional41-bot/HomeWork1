import os

class Task:
    def __init__(self,title):
        self.title = title
        self.is_done = "Не выполнено"

    def mark_done(self):
        self.is_done = "Выполнено"

    def __str__(self):
        return f"{self.title} - {self.is_done}"


class TaskManager:
    def __init__(self,filename ="tasks.txt"):

        self.filename = filename
        self.tasks = []
        self.load_from_file()


    def add_task(self ,title):
        task = Task(title)
        self.tasks.append(task)

    def mark_task_done(self ,title):
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                return True
        return False


    def show_tasks(self):

        for i, task in enumerate(self.tasks , 1):
            print(f"{i}. {task.title}")

    def save_to_file(self):

        with open(self.filename, 'w', encoding='utf-8') as f:
            for task in self.tasks:
                f.write(f"{task.title}|{task.is_done}\n")

    def load_from_file(self):

            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip():
                            title, status = line.strip().split('|')
                            task = Task(title)
                            if status == "Выполнено":
                                task.mark_done()
                            self.tasks.append(task)