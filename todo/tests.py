from django.test import TestCase
from .models import Todo

# Create your tests here.

class TodoTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(todo_body='O corpo')

    def test_corpo_criado(self):
        corpo = Todo.objects.all()[0].todo_body
        self.assertEqual(corpo,'O corpo')
