from classroom_template import Classroom
from student_template import Student
import pytest

def create_classroom():
    new_classroom = Classroom("Chemistry", "Dr. O'Niel", "Mon/Wed 2PM - 4PM PST")
    return new_classroom

# def create_student():
#     new_student = Student("Jayce Azua", 27)
#     return new_student

def test_create_classroom():
    new_classroom = create_classroom()
    new_classroom_2 = Classroom("Computer Science with Python", "Instructor Mike Kane", "Mon 10:30AM PST")
    assert new_classroom.class_name == "Chemistry"
    assert new_classroom_2.class_name == "Computer Science with Python"
    assert new_classroom.teacher_name != "Instructor Mike Kane"
    assert new_classroom.teacher_name == "Dr. O'Niel"
    assert len(new_classroom_2.roster) == 0
    assert len(new_classroom.roster) != 1
    assert new_classroom.next_available_student_number == 0
    assert new_classroom_2.next_available_student_number != 1
    assert new_classroom.class_day_and_time == "Mon/Wed 2PM - 4PM PST"
    assert new_classroom_2.class_day_and_time == "Mon 10:30AM PST"

def test_enroll_student():
    new_classroom = create_classroom()
    assert new_classroom.next_available_student_number == 0
    new_classroom.enroll_student("Josh")
    assert new_classroom.next_available_student_number == 1
    new_classroom.enroll_student("Roan")
    assert len(new_classroom.roster) == 2
    assert new_classroom.roster[1].name == "Josh"
    assert new_classroom.roster[2].name == "Roan"
    assert new_classroom.roster[1].student_ID != 0
    assert new_classroom.roster[2].student_ID == 2
    assert new_classroom.roster[1] != new_classroom.roster[2]
    assert new_classroom.next_available_student_number == 2
    assert 2 in new_classroom.roster
