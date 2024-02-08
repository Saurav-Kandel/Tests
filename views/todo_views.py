from flask import jsonify, request, abort
from flask.views import View

from services.todo_service import TodoService


class AllTaskView(View):
    def dispatch_request(self):
        todo_tasks = TodoService.get_all_tasks()
        if len(todo_tasks) > 0:
            return todo_tasks
        else:
            return jsonify('There are no tasks to do as the moment')


class SpecificTaskView(View):
    def dispatch_request(self, id):
        specific_task = TodoService.get_specific_task(id)
        if len(specific_task) > 0:
            return specific_task
        else:
            return jsonify('The task doesnt exits !')


class AddTaskView(View):
    methods = ['POST']
    
    def dispatch_request(self):
        request_body = request.get_json()
        content = request_body.get("content")
        if not content:
            abort(400, "Content is required")
        if not isinstance(content, str):
            abort(400, "Content should be string")

        added_task = TodoService.add_task(content)
        if len(added_task) > 0:
            return added_task
        else:
            return jsonify('Could not get the newly added task !')
