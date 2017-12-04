################################################################################
### class ModuleElement ###
class ModuleElement(object):
    def __init__(self, module):
        "constructor for class module element"
        # store module as instance variable:
        self._module = module


    def add_important_date(self, kind_of_date, date):
        "add a date to the module's date dictionary"
        self._module._dates.append((kind_of_date, date))

################################################################################
### class Lesson ###
class Lesson(ModuleElement):
    def __init__(self, module):
        "constructor for class lesson"
        # call super class constructor:
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        "add a lesson to the date dictionary"
        ModuleElement.add_important_date(self, "Lesson", date)

################################################################################
### class Lab ###
class Lab(ModuleElement):
    def __init__(self, module):
        "constructor for class lab"
        # call super class constructor:
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        "add a lab session to the date dictionary"
        ModuleElement.add_important_date(self, "Lab Session", date)

################################################################################
### class Midterm ###
class Midterm(ModuleElement):
    def __init__(self, module):
        "constructor for class midterm"
        # call super class constructor:
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        "add a midterm to the date dictionary"
        ModuleElement.add_important_date(self, "Midterm", date)

################################################################################
### class FinalExam ###
class FinalExam(ModuleElement):
    def __init__(self, module):
        "constructor for class final exam"
        # call super class constructor:
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        "add a final exam to the date dictionary"
        ModuleElement.add_important_date(self, "Final Exam", date)

################################################################################
### Test cases in file student.py """

