from module import *
from moduleElement import *

################################################################################
### class Student ###
class Student(object):
    def __init__(self, name):
        "constructor for class student"
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self, module):
        "adds a module to the module list of the student"
        self.modules.append(module)
        self.grades[module] = module.get_grade()

    def get_list_modules(self):
        "prints all the modules of the student"
        print("Modules of Student {0:s}:".format(self.name))
        for module in self.modules:
            print("\t{0:s}".format(module._title))

    def get_grades(self):
        "prints all the modules with the corresponding grade"
        print("Grades of Student {0:s}:".format(self.name))
        for module, grade in self.grades.items():
            #if a module has no grade, a special message is printed
            if grade:
                print("\t{0:s}: {1:d}".format(module._title, grade))
            else:
                print("\tModule {0:s} has not yet been graded".format(module._title))

################################################################################
### test cases
info1 = Course(6,"Info 1",1)
info1.add_module_element(Midterm,"31.10.2017")
info1.add_module_element(FinalExam,"20.12.2017")
info1.get_important_dates_overview()
print(info1)
# expected output:
# Important dates for Info 1:
#	Midterm on 31.10.2017
#	Final Exam on 20.12.2017
# Course: Info 1

math1 = Course(6, "Mathematik I", 1)
math1.add_module_element(Midterm,"18.12.2017")
math1.get_important_dates_overview()
# expected output:
# Important dates for Mathematik I:
#	Midterm on 18.12.2017


print(Module.module_count)
# expected output:
# 2

thesis = Thesis(18,"Bachelor Thesis",6,"A promising research topic on Software Engineering","SEAL")
print(thesis)
# expected output:
# Bachelor Thesison the topic: A promising research topic on Software Engineering in the Research Group SEAL


sem = Seminar(3,"Seminar in Software Engineering",4,"A Seminar topic")
print(sem)
# expected output:
# Seminar in Software Engineering under the topic: A Seminar topic

info1.set_grade(6)
print(info1.get_grade())
# expected output:
# 6

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
