import unittest
from employee import Employee

class TestEmployeeCase(unittest.TestCase):

    def setUp(self):
        self.my_emploeyy = Employee("123", "gou", 3000)
        self.name = "gou 123"
        self.money = 3000

    def test_give_default_raise(self):
        self.my_emploeyy.give_raise()
        self.assertEqual(self.money + 5000, self.my_emploeyy.money)

    def test_give_custon_raise(self):
        self.my_emploeyy.give_raise(3000)
        self.assertEqual(self.money + 3000, self.my_emploeyy.money)

unittest.main()