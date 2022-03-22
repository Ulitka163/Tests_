import unittest
from task_2_1 import *


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print('===> setUp')

    def tearDown(self) -> None:
        print('===> tearDown')

    def test_people_name(self):
        self.assertEqual(people_name('2207 876234'), "Василий Гупкин")

    @unittest.expectedFailure
    def test_people_name_failure(self):
        self.assertEqual(people_name('2207 876234'), 'dfg')

    def test_number_directories(self):
        self.assertEqual(number_directories('2207 876234'), '1')

    @unittest.expectedFailure
    def test_number_directories_failure(self):
        self.assertEqual(number_directories('2207 876234'), '5')

    def test_delete(self):
        self.assertTrue(delete('11-2'))

    def test_add_shelf(self):
        self.assertTrue(add_shelf('5'))
        self.assertFalse(add_shelf('1'))

    def test_add_documents(self):
        self.assertTrue(add_documents('file', '45698', 'Jone', '3'))
        self.assertFalse(add_documents('file', '43333', 'Juli', '9'))

    def test_list_documents(self):
        self.assertTrue(list_documents())

    def test_move(self):
        self.assertTrue(move('10006', '3')[1])
        self.assertFalse(move('11-2', '6')[1])
        self.assertFalse(move('4568', '2')[1])
