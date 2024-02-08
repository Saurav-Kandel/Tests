import unittest
import datetime
from unittest.mock import patch

from models.todo import Todo
from services.todo_service import TodoService
from repositories.todo_repository import TodoRepository


class TestTodoService(unittest.TestCase):

    @patch.object(TodoRepository, "get_all_tasks")
    def test_get_all_tasks_when_no_tasks_exist(self, get_tasks_mock):
        get_tasks_mock.return_value = []
        all_tasks = TodoService.get_all_tasks()
        self.assertEqual(all_tasks, [])
    
    @patch.object(TodoRepository, "get_all_tasks")
    def test_get_all_tasks_when_tasks_exist(self, get_tasks_mock):
        mock_id = 1
        mock_date_created = datetime.datetime.utcnow()
        mock_content = "All task"
        mock_todo = Todo(id=mock_id, date_created=mock_date_created, content=mock_content)
        get_tasks_mock.return_value = [mock_todo]
        all_tasks = TodoService.get_all_tasks()
        expected_result = [{
            'id': mock_id,
            'content': mock_content,
            'date-created': mock_date_created,
        }]
        self.assertEqual(all_tasks, expected_result)
    
    @patch.object(TodoRepository, "get_specific_task")
    def test_get_specific_task_when_no_specific_task_exist(self, get_tasks_mock):
        get_tasks_mock.return_value = {}
        specific_task = TodoService.get_specific_task(10)
        expected_result = {}
        self.assertEqual(specific_task, expected_result)
    
    @patch.object(TodoRepository, "get_specific_task")
    def test_get_specific_task_when_task_exist(self, get_tasks_mock):
        mock_id = 2
        mock_content = "Specific Task"
        get_tasks_mock.return_value, expected_result = self.mock_todo_task(mock_id, mock_content)
        specific_task = TodoService.get_specific_task(mock_id)
        self.assertEqual(specific_task, expected_result)

    @patch.object(TodoRepository, "add_task")
    def test_add_task_when_task_added(self, get_tasks_mock):
        mock_id = 11
        mock_content = "Newly Added Task"
        get_tasks_mock.return_value, expected_result = self.mock_todo_task(mock_id, mock_content)
        added_task = TodoService.add_task(mock_content)
        self.assertEqual(added_task, expected_result)
    
    @patch.object(TodoRepository, "add_task")
    def test_add_task_when_no_task_added(self, get_tasks_mock):
        mock_content = "Newly Added Task"
        get_tasks_mock.return_value = {}
        added_task = TodoService.add_task(mock_content)
        expected_result = {}
        self.assertEqual(added_task, expected_result)
    
    def mock_todo_task(self, id, content):
        mock_task = Todo(id=id, date_created=datetime.datetime.utcnow, content=content)
        expected_result = {
            'id': mock_task.id,
            'content': mock_task.content,
            'date-created': mock_task.date_created,
        }
        return mock_task, expected_result
