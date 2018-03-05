from student_template import Student

class Classroom(object):
    '''
    Classroom object that will act as high-level interface for operations on classroom
    full of students.

    Each Classroom object contains the following attributes:

    _____Attributes_______

    class_name:  String. The name of the class.

    teacher_name: String.  The name of the teacher responsible for the class.

    class_day_and_time:  The days the class meets.

    roster: Dictionary {student_ID (Int): student_object (Student)}. A dictionary of
    students enrolled in the class.  Dictionary is empty on initialization.

    _____Methods________

    init(self, class_name, teacher_name, class_day_and_time):
        - Expects all inputs (aside from self) to be passed as a String.

    enroll_student(student_name):
        - Expects student_name as string.
        - Creates a new student object.
        - Sets the new student's student_ID to self.next_available_student_number
        - increments self.next_available_student_number by 1.
        - adds to roster dictionary, with new student's student_ID as key and student
            object as value.

    add_assignment_for_student(student_name, assignment_name, grade):
        - searches roster for student with student_name.
            - if student does not exist, prints and error message.
        - calls student object's add_assignment() method with assignment_name and grade
            as inputs.

    add_assignment_for_class(assignment_name):
        - Expects assignment_name as String.
        - Loops through each student in self.roster.values().
        - For each student, prints message asking teacher to add grade for student.name
        - Once user has entered input, validates input using _is_valid_grade() method.
            - if input is not valid, asks user again for input.
        - If user input is valid, calls student's add_assignment() method and continues
            through loop.

    drop_assignment_for_student(student_name, assignment_name):
        -  Expects student_name as String.
        -  Expects assignment_name as String.
        -  Loops through roster.values() and finds student with student_name passed in.
            - If student does not exist, prints error message saying so.
        -  Calls student's delete_assignment() method, with assignment_name as input.

    drop_assignment_for_class(assignment_name):
        -  Expects assignment_name as String.
        -  Loops through each student in self.roster.values()
            - Calls student's delete_assignment() method with assignment_name as input.

    get_student_GPA(student_name):
        - Expects student_name as String.
        - Searches self.roster for student with student_name.
            - If no student with that name, prints error message saying so.
        - If found, returns that student's self.GPA attribute.

    get_class_average():
        -  Expects no inputs.
        -  Iterates through all students in self.roster.values() and returns the average
            of their GPA attributes.
    '''

    def __init__(self, class_name, teacher_name, class_day_and_time):
        self.class_name = class_name
        self.teacher_name = teacher_name
        self.class_day_and_time = class_day_and_time
        self.roster = {}
        self.next_available_student_number = 1

    def enroll_student(self, student_name):
        # - Expects student_name as string.
        # - Creates a new student object.
        student_ID = self.next_available_student_number
        # - Sets the new student's student_ID to self.next_available_student_number
        new_student = Student(student_name, student_ID)
        # - increments self.next_available_student_number by 1.
        self.next_available_student_number += 1
        # - adds to roster dictionary, with new student's student_ID as key and student object as value.
        self.roster[new_student.student_ID] = new_student
        print("{} was enrolled successfully in {}.".format(new_student.name, self.class_name))

# I created this one on my own :D
    def withdraw_student(self, student_name):
        # - searches roster for student with student_name.
        for student in self.roster.values():
        # if the parameter matches
            if student.name is student_name:
        # delete that student
                del self.roster[student.student_ID]
        # let the teacher know the student is not enrolled.
            else:
                print("{} is not enrolled in this {} class.".format(student_name, self.class_name))

    def add_assignment_for_student(self, student_name, assignment_name, grade):
        '''Adds an assignment and corresponding grade for an individual student.'''
        # - searches roster for student with student_name.
        for student in self.roster.values():
            if student.name is student_name:
        # - calls student object's add_assignment() method with assignment_name and grade as inputs.
                student.add_assignment(assignment_name, grade)
        #     - if student does not exist, prints and error message.
            else:
                print("{} is not enrolled in this {} class.".format(student_name, self.class_name))


    def _is_valid_grade(self, grade):
        # look it up and did not cheat.
        try:
            valid_grade = float(grade)
            if valid_grade >= 0:
                return True
        # there are different Error types this being the most accurate
        except ValueError:
            return False

    def add_assignment_for_class(self, assignment_name):
        # - Expects assignment_name as String.
        # - Loops through each student in self.roster.values().
        for student in self.roster.values():
        # - For each student, prints message asking teacher to add grade for student.name
            grade = ""
        # - Once user has entered input, validates input using _is_valid_grade() method.
            while not self._is_valid_grade(grade):
        #     - if input is not valid, asks user again for input.
                grade = float(input("Enter {}'s grade for assignment {} --> ".format(student.name, assignment_name)))
        # - If user input is valid, calls student's add_assignment() method and continues through loop.
            student.add_assignment(assignment_name, grade)


    def drop_assignment_for_student(self, student_name, assignment_name):
        # -  Expects student_name as String.
        # -  Expects assignment_name as String.
        # -  Loops through roster.values() and finds student with student_name passed in.
        #     - If student does not exist, prints error message saying so.
        # -  Calls student's delete_assignment() method, with assignment_name as input.
        pass


    def drop_assignment_for_class(self, assignment_name):
        # -  Expects assignment_name as String.
        # -  Loops through each student in self.roster.values()
        #     - Calls student's delete_assignment() method with assignment_name as input.
        pass


    def get_student_GPA(self, student_name):
        # - Expects student_name as String.
        # - Searches self.roster for student with student_name.
        for student in self.roster.values():
            # - If found, returns that student's self.GPA attribute.
            if student.name is student_name:
                return student.GPA
        #     - If no student with that name, prints error message saying so.
            else:
                print("{} is not enrolled in this {} class.".format(student_name, self.class_name))

    def get_class_average(self):
        # -  Expects no inputs.
        # -  Iterates through all students in self.roster.values() and returns the average of their GPA attributes.

        pass
