__author__ = 'rburke'

import json as js
import task_status
from datetime import date
from dateutil import parser

class TaskIllegalStatusException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self)

class TaskIllegalPriorityException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self)

class TaskIllegalPriorityException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self)

class TaskIllegalEffortException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self)

class TaskIllegalScheduleException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self)

class TaskIllegalValuesException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self)

class TaskIllegalDateException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self)

class Task:

    _data = { }

    def __init__(self):
        self._data['status'] = task_status.TaskStatus.NULL

    # String input is assumed to be a JSON object
    # We do not assign directly from the JSON dictionary so that we have control over the contents here
    def __init__(self, str):
        str_dict = js.loads(str)
        # Does not check for uniqueness of id
        self._data['id'] = str_dict['id']
        self._data['name'] = str_dict['name']
        self._data['description'] = str_dict['description']
        self._data['template'] = str_dict['template']

        # Values must be a list
        if 'values' in str_dict:
           self._data['values'] = str_dict['values']
        else:
            self._data['values'] = []

        self._data['status'] = str_dict['status']
        self._data['priority'] = str_dict['priority']
        self._data['effort'] = str_dict['effort']
        self._data['schedule'] = str_dict['schedule']

        if 'date_active' in str_dict:
            date_str = str_dict['date_active']
            date_active = parser.parse(date_str)
            self._data['date_active'] = date_active

        if 'date_accepted' in str_dict:
            date_str = str_dict['date_accepted']
            date_accepted = parser.parse(date_str)
            self._data['date_accepted'] = date_accepted

        if 'date_completed' in str_dict:
            date_str = str_dict['date_completed']
            date_completed = parser.parse(date_str)
            self._data['date_completed'] = date_completed


    def getId(self):
        return self._data['id']

    def getName(self):
        return self._data['name']

    def getDescription(self):
        return self._data['description']

    def getTemplate(self):
        return self._data['template']

    def getTemplateFormatted(self):
        values = self._data['values']
        if len(values) == 0:
            return "Error: no values to format"
        return self._data['template'].format(*values)

    def setValues(self, values):
        if type(values) is list:
            self._data['values'] = values
        else:
            raise TaskIllegalValuesException(values)

    def hasValues(self):
        return len(self._data['values']) > 0

    def getStatus(self):
        return self._data['status']

    def setStatus(self, value):
        if type(value) is int:
            self._data['status'] = value
        else:
            raise TaskIllegalStatusException(value)

    def getPriority(self):
        return self._data['priority']

    def setPriority(self, value):
        if type(value) is float:
            self._data['priority'] = value
        else:
            raise TaskIllegalPriorityException(value)

    def getEffort(self):
        return self._data['effort']

    def setEffort(self, value):
        if type(value) is float:
            self._data['priority'] = value
        else:
            raise TaskIllegalEffortException(value)

    def getSchedule(self):
        return self._data['schedule']

    def setSchedule(self, value):
        if type(value) is int:
            self._data['schedule'] = value
        else:
            raise TaskIllegalScheduleException(value)

    def getDateActive(self):
        return self._data['date_active']

    def setDateActive(self, value):
        if type(value) is basestring:
            value = parser.parse(value)
        if type(value) is date:
            self._data['date_active'] = value
        else:
            raise TaskIllegalDateException(value)

    def getDateAccepted(self):
        return self._data['date_accepted']

    def setDateAccepted(self, value):
        if type(value) is basestring:
            value = parser.parse(value)
        if type(value) is date:
            self._data['date_accepted'] = value
        else:
            raise TaskIllegalDateException(value)

    def getDateCompleted(self):
        return self._data['date_accepted']

    def setDateCompleted(self, value):
        if type(value) is basestring:
            value = parser.parse(value)
        if type(value) is date:
            self._data['date_completed'] = value
        else:
            raise TaskIllegalDateException(value)