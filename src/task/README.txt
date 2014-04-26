The task package has the following modules:

TaskLibrary:
    This is a dictionary of Task objects, indexed by ID.

Task:
    This is the main object for tasks. It holds the following data:
        ID: unique integer ID
        name: a short name starting with a verb. Ex. "Get Water"
        description: a longer description that explains why the task is important. Ex. "In an emergency, water supply
           may be unavailable or contaminated. You should have enough water for drinking and for personal tasks like
           washing and brushing teeth."
        template: a string expressed in the Python format specification language. This will turn into the entry in the
           task list when it is specified. Ex. "Buy { } gallons for water for your family of { }."
        values: These are the values that will be interpolated into the format string. If this list is missing, then
           the task is a "uninitialized task". If there is a value (even if it is an empty list), then the task is an
           "initialized task".
        status: an integer taking on the following values:
            0 = null, which means the task has no content
            1 = uninitialized, which means that the task has content, but there are no values associated with the template
            2 = pending, which means the task can given to the user, but hasn't come up yet in the schedule
            3 = the user has accepted the task, will be foregrounded on the task list
            4 = completed
            others?
        priority: a floating point value from 0..1 reflecting the priority of the task. Maybe user-specific?
        effort: a floating point value from 0..1 reflecting the relative effort associated with the task. Not sure how
            we plan to make use of this?
        schedule: an integer reflecting the task schedule. If = 0, it is a one-time task. If > 0, it represents a
            recurring task and this number is the number of days after completion of the task that the next one
            should be scheduled.
        date_active: the date that the task becomes active
        date_accepted: the date that the user accepted the task
        date_completed: the date that the user completed the task

TaskLoader:
    Takes a file path or stream and instantiate a task library.





Note: in this version, we are not supporting merged tasks (water for people and water for pets are separate tasks.)

it = f.parse("foo{} bar{:<30} {}")
print len([c for a,b,c,d in it])

for a,b,c,d in it:
    print "a= {}, b={}, c={}, d={}".format(a,b,c,d)
