from repositories.todo_repository import TodoRepository
from models.todo import Todo
from typing import List, Dict, Any


class TodoService():

    @classmethod
    def get_all_tasks(cls) -> List[Dict[str, Any]]:
        todo_tasks = TodoRepository.get_all_tasks()
        all_tasks = []
        for task in todo_tasks:
            tasks = {
                'id': task.id,
                'content': task.content,
                'date-created': task.date_created,
            }
            all_tasks.append(tasks)
        return all_tasks

    @classmethod
    def get_specific_task(cls, id: int) -> Dict[str, Any]:
        try:
            specific_task = TodoRepository.get_specific_task(id)
        except:
            raise Exception
        print(specific_task)
        task = {}
        if specific_task:
            task = {
                'id': specific_task.id,
                'content': specific_task.content,
                'date-created': specific_task.date_created,
            }
        return task
        
    @classmethod
    def add_task(cls, content: str) -> Dict[str, Any]:
        new_task = Todo(content=content)
        task = TodoRepository.add_task(new_task)
        added_task = {}
        if task:
            added_task = {
                    'id': task.id,
                    'content': task.content,
                    'date-created': task.date_created,
                }
        return added_task
