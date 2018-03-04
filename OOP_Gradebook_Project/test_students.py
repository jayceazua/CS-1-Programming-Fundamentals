from student_template import Student
import pytest

def create_student():
    new_student = Student("Jayce Azua", 27)
    return new_student

def test_create_student():
    new_student = create_student()
    assert new_student.name == "Jayce Azua"
    assert new_student.student_ID == 27
    assert new_student.GPA == None
    assert new_student.assignments.__len__() == 0

def test_add_assignment():
    new_student = create_student()
    new_student.add_assignment("Hangman", 100)
    assert new_student.assignments.__len__() == 1
    assert new_student.GPA == 100
    new_student.add_assignment("GradeBook_OOP", 98)
    assert new_student.assignments["GradeBook_OOP"] == 98
    assert new_student.assignments.__len__() == 2
    assert new_student.GPA == 99

def test_delete_assignment():
    new_student = create_student()
    new_student.add_assignment('English', 98)
    new_student.add_assignment('Chemistry', 87)
    assert len(new_student.assignments) == 2
    new_student.delete_assignment('English')
    assert len(new_student.assignments) == 1
    new_student.delete_assignment('Math') == 'Assignment does not exist.'

def test_update_grade_for_assignment():
    new_student = create_student()
    new_student.add_assignment('English', 98)
    new_student.add_assignment('Chemistry', 87)
    assert new_student.assignments["English"] == 98
    new_student.update_grade_for_assignment('English', 70)
    assert new_student.assignments['English'] == 70
    new_student.update_grade_for_assignment('Chemistry', 70)
    assert new_student.assignments['Chemistry'] == 70
    assert new_student.GPA == 70

def test_update_grade_in_class():
    new_student = create_student()
    assert new_student.GPA == None
    new_student.add_assignment("GradeBook_OOP", 100)
    assert new_student.GPA == 100
    new_student.add_assignment("Hangman Game", 100)
    assert new_student.GPA == 100
    new_student.update_grade_for_assignment('Markov Chain', 100)
    assert new_student.GPA == 100
