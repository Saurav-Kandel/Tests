from app import db
from models.todo import Todo


class TodoRepository():

    @classmethod
    def get_all_tasks(cls):
        return Todo.query.order_by(Todo.date_created).all()

    @classmethod
    def get_specific_task(cls, id):
        return Todo.query.get(id)
    
    @classmethod
    def add_task(cls, new_task):
        db.session.add(new_task)
        db.session.commit()
        task = Todo.query.get(new_task.id)
        return task
