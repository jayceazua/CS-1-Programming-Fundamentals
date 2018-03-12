from person import Person
import pytest


def create_person():
    person = Person(0, True)
    return person

def test_create_person():
    person = create_person()
    assert person._id == 0
    assert person.is_alive == True
    assert person.is_vaccinated == True
    assert person.infected == None

def test_did_survive_infection():
    pass
