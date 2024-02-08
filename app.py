from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.init_app(app)
    from views.todo_views import AllTaskView
    from views.todo_views import SpecificTaskView
    from views.todo_views import AddTaskView

    app.add_url_rule('/api/todo', view_func=AllTaskView.as_view("all_task"))
    app.add_url_rule('/api/todo/<int:id>', view_func=SpecificTaskView.as_view("specific_task"))
    app.add_url_rule('/api/todo/add', view_func=AddTaskView.as_view("add_task"))

    return app

# if __name__ == "__main__":
#     app.run(debug=True)
