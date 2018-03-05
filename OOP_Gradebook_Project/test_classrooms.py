from classroom_template import Classroom
from student_template import Student
import pytest

def create_classroom():
    new_classroom = Classroom("Chemistry", "Dr. O'Niel", "Mon/Wed 2PM - 4PM PST")
    return new_classroom

def test_create_classroom():
    new_classroom = create_classroom()
    new_classroom_2 = Classroom("Computer Science with Python", "Instructor Mike Kane", "Mon 10:30AM PST")
    assert new_classroom.class_name == "Chemistry"
    assert new_classroom_2.class_name == "Computer Science with Python"
    assert new_classroom.teacher_name != "Instructor Mike Kane"
    assert new_classroom.teacher_name == "Dr. O'Niel"
    assert len(new_classroom_2.roster) == 0
    assert len(new_classroom.roster) != 1
    assert new_classroom.next_available_student_number == 1
    assert new_classroom_2.next_available_student_number != 0
    assert new_classroom.class_day_and_time == "Mon/Wed 2PM - 4PM PST"
    assert new_classroom_2.class_day_and_time == "Mon 10:30AM PST"

def test_enroll_student():
    new_classroom = create_classroom()
    assert new_classroom.next_available_student_number == 1
    new_classroom.enroll_student("Josh")
    assert new_classroom.next_available_student_number == 2
    new_classroom.enroll_student("Roan")
    assert len(new_classroom.roster) == 2
    assert new_classroom.roster[1].name == "Josh"
    assert new_classroom.roster[2].name == "Roan"
    assert new_classroom.roster[1].student_ID != 2
    assert new_classroom.roster[2].student_ID == 2
    assert new_classroom.roster[1] != new_classroom.roster[2]
    assert new_classroom.next_available_student_number == 3

# I created this one on my own :D
def test_withdraw_student():
    new_classroom = create_classroom()
    new_classroom.enroll_student("Roan")
    assert len(new_classroom.roster) == 1
    new_classroom.enroll_student("Josh")
    new_classroom.withdraw_student("Roan")
    assert len(new_classroom.roster) == 1
    new_classroom.withdraw_student("Josh")
    assert len(new_classroom.roster) == 0
    assert new_classroom.withdraw_student("Roan") == None
    assert new_classroom.withdraw_student("Josh") == None

def test_add_assignment_for_student():
    new_classroom = create_classroom()
    new_classroom.enroll_student("Jayce")
    student = new_classroom.roster[1]
    assert student.name == "Jayce"
    new_classroom.add_assignment_for_student("Jayce", "Research Paper", 98)
    assert len(student.assignments) == 1
    assert student.assignments["Research Paper"] == 98
    assert new_classroom.add_assignment_for_student("Ryan", "Research Paper", 98) == None

def test_get_student_GPA():
    new_classroom = create_classroom()
    student = Student("Jayce", 1)
    new_classroom.roster[1] = student
    new_classroom.add_assignment_for_student("Jayce", "Research Paper", 98)
    student.add_assignment("Atoms and DNA", 91)
    assert student.assignments["Atoms and DNA"] == 91
    assert new_classroom.get_student_GPA("Jayce") == 94.5

def test_add_assignment_for_class():
    classroom = create_classroom()
    student_1 = Student("Jayce", 1)
    student_2 = Student("Katherine", 2)
    classroom.roster[1] = student_1
    classroom.roster[2] = student_2
    classroom.add_assignment_for_class("Sex Education")
    assert student_1.assignments["Sex Education"] == 98.7
    assert student_2.assignments["Sex Education"] == 78.3
