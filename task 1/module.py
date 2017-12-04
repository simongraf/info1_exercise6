from moduleElement import *
### class Module ###
class Module(object):
    module_count = 0

    def __init__(self, ects, title, semester, grade=None):
        "constructor for class module"
        Module.module_count += 1
        self._ects = ects
        self._title = title
        self._semester = semester
        self._grade = grade
        self._dates = []
        self.__elements = []

    def get_title(self):
        "returns the title of the module"
        return self._title

    def set_grade(self, new_grade):
        "set the grade to a given value"
        self._grade = new_grade

    def get_grade(self):
        "returns the grade of the module"
        return self._grade

    def get_important_dates_overview(self):
        "prints all the important dates for a module"
        print("Important dates for {0:s}:".format(self._title))
        for kind,date in self._dates:
            print("\t{0:s} on {1:s}".format(kind,date))

    def add_module_element(self, class_name, date):
        "add a new module element to the elements list"
        new_object = class_name(self)
        new_object.add_important_date(date)
        self.__elements.append(new_object)

################################################################################
### class Course ###
class Course(Module):
    "Constructor of the superclass is used"

    def __str__(self):
        "prints the title of the course"
        return "Course: {0:s}".format(self._title)

################################################################################
### class Seminar ###
class Seminar(Module):
    def __init__(self, ects, title, semester, topic):
        "Constructor of the seminar"
        # call super class constructor:
        Module.__init__(self,ects,title,semester)
        self._topic = topic

    def __str__(self):
        "prints the title of the seminar"
        return "Seminar in {0:s} under the topic: {1:s}".format(self._title, self._topic)

    def get_topic(self):
        "returns the topic of the seminar"
        return self._topic

################################################################################
### class Thesis ###
class Thesis(Module):
    def __init__(self, ects, title, semester, topic, research_group):
        "Constructor of the thesis"
        # call super class constructor:
        Module.__init__(self,ects,title,semester)
        self._topic = topic
        self._research_group = research_group

    def __str__(self):
        "prints the title of the thesis"
        return "Bachelor Thesis on the topic: {0:s} in the Research Group {1:s}".format(self._topic, self._research_group)

    def get_topic(self):
        "returns the topic of the thesis"
        return self._topic

    def get_research_group(self):
        "returns the research groupt of the thesis"
        return self._research_group

################################################################################
### Test cases in file student.py """