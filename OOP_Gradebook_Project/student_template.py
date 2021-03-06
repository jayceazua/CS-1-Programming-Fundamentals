
class Student(object):
    '''Class of student objects that will populate each class roster.

    Each student object contains the following attributes:

    _____Attributes_______

    _student_ID: Int.  A unique integer identifier assigned to each student at the object's creation.

    name: String.  The name of the student.

    GPA: Float.  A running average of the student's overall grade in the class. Will be set to None
        until an assignment has been graded and passed to the Assignments dictionary.

    assignments: Dictionary {Assignment name (Str): Grade (Float)}.  A record of all assignments
        the student has completed, and the grade he or she has earned on each.
        Dictionary is empty on initialization

    _____Methods________

        __init__(self, name, student_ID):
            -Requires the student's name passed as a String.
            -Requires the student's student_ID number passed as an Int.
            -Initially sets GPA to None.
            -Initially sets Assignments to an empty Dictionary.

        add_assignment(self, name, grade):
            expects name as string.
            expects grade as float.
            Adds assignment to Assignment attribute with name as key, grade as value. When finished,
            calls _update_grade_in_class() method to recalculate student average.

        update_assignment_grade(self, name, grade):
            expects name as string.
            expects grade as float.
            Used to update the grade of an assignment that already exists.
            Uses name argument as key in Assignment Dictionary, and then updates the value to the grade argument.
            Raises an error if name attribute does not already exist in the assignments dictionary.  Calls
            _update_grade_in_class() helper method after updating.

        _update_grade_in_class(self):
        Expects no inputs.
        Calculates the student's grade in class by dividing the student's cumulative assignment scores
            by the number of total assignments in the Assignment Dictionary. Updates self.GPA with this
            value.

        delete_assignment(self, assignment_name, grade):
            -Expects assignment name as string.
            -Expects grade as float.
            -Deletes assignment with 'assignment_name' as key from self.assignments (along with corresponding grade.)
            -If assignment exists, should delete assignment and then print confirmation that assignment has been
            successfully deleted.
            -If assignment_name is not found in self.assignments, should raise an error telling the user that
            this assignment does not exist for this student.
     '''
    def __init__(self, name, student_ID):
         self.name = name
         self.student_ID = student_ID
         self.GPA = None
         self.assignments = {}

    def _update_grade_in_class(self):
        # Expects no inputs.
            # Calculates the student's total grade in class
            total_grades = sum(self.assignments.values())
            # Calculates the number of total assignments in the Assignment Dictionary
            total_assignments = len(self.assignments)
            # Updates self.GPA with this value by dividing the student's cumulative assignment scores with total_assignments
            self.GPA = total_grades / total_assignments



    def update_grade_for_assignment(self, assignment_name, grade):
        # expects name as string.
        # expects grade as float.
        # Used to update the grade of an assignment that already exists.
        if assignment_name in self.assignments:
        # Uses name argument as key in Assignment Dictionary, and then updates the value to the grade argument.
            self.assignments[assignment_name] = grade
            # Calls _update_grade_in_class() helper method after updating.
            self._update_grade_in_class()
        else:
            # Raises an error if name attribute does not already exist in the assignments dictionary.
            print("Assignment does not exist.")

    def delete_assignment(self, assignment_name):
        # -Expects assignment name as string.
        # -Expects grade as float.
        # -Deletes assignment with 'assignment_name' as key from self.assignments (along with corresponding grade.)
        # -If assignment exists, should delete assignment and then print confirmation that assignment has been successfully deleted.
        if assignment_name in self.assignments:
            del self.assignments[assignment_name]
        # -If assignment_name is not found in self.assignments, should raise an error telling the user that this assignment does not exist for this student.
        else:
            print("Assignment does not exist.")

    def add_assignment(self, assignment_name, grade):
        # expects name as string.
        # expects grade as float.
        # Adds assignment to Assignment attribute with name as key, grade as value.
        self.assignments[assignment_name] = float(grade)
        # When finished, calls _update_grade_in_class() method to recalculate student average.
        self._update_grade_in_class()
