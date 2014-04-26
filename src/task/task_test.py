__author__ = 'rburke'

import unittest

import task
from datetime import datetime

class TestTaskLoading(unittest.TestCase):
    def setUp(self):
        self.task_string = '{ "id": 12121, "name": "Test", "description": "This is a test task", \
        "template": "This is a test template with two values {} {}", "status": 0, "priority": 0.5, \
        "effort": 0.5, "schedule": 0, "date_active": "2014-04-25" }'

    def test_parse(self):
        self.tsk = task.Task(self.task_string)

        self.assertEqual(self.tsk.getId(), 12121)
        self.assertEqual(self.tsk.getName(), "Test")
        self.assertEqual(self.tsk.getDescription(), "This is a test task")
        self.assertEqual(self.tsk.getTemplate(), "This is a test template with two values {} {}")
        self.assertFalse(self.tsk.hasValues())
        self.assertEqual(self.tsk.getStatus(), 0)
        self.assertAlmostEqual(self.tsk.getPriority(), 0.5)
        self.assertAlmostEqual(self.tsk.getEffort(), 0.5)
        self.assertEqual(self.tsk.getSchedule(), 0)
        self.assertEqual(self.tsk.getDateActive(), datetime(2014,04,25,0,0))

    def test_format(self):
        self.tsk.setValues(['a', 'b'])
        self.assertEqual(self.tsk.getTemplateFormatted(), "This is a test template with two values a b")

    def test_bad_values(self):
        self.assertRaises(task.TaskIllegalValuesException, self.tsk.setValues('foo'))

    def test_set_dates(self):
        self.tsk.setDateActive("2014-04-01")
        self.tsk.setDateAccepted(datetime(2014, 04, 01))
        self.tsk.setDateCompleted("2014-05-01")




if __name__ == '__main__':
    unittest.main()