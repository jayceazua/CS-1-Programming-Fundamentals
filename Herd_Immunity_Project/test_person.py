from person import Person
from simulation import Simulation
import pytest


def create_simulation():
    pop_size = 10
    vacc_percentage = 0.90
    virus_name = 'Zombies'
    mortality_rate = 0.70
    basic_repro_num = 0.25
    initial_infected = 0
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected)
    return simulation


def create_person():
    person = Person(0, True)
    return person

def test_create_person():
    person = create_person()
    person_2 = Person(1, False, False)
    person_3 = Person(2, False, True)
    assert person._id == 0
    assert person_2._id == 1
    assert person_3._id == 2
    assert person.is_alive == True
    assert person_2.is_alive == True
    assert person.is_vaccinated == True
    assert person_2.is_vaccinated == False
    assert person_3.is_vaccinated == False
    assert person.infected == False
    assert person_2.infected == False
    assert person_3.infected == True



def test_did_survive_infection():
    simulation = create_simulation()
    person = Person(11, False, True)
    assert person.is_alive == True
    assert person.is_vaccinated == False
    assert person.infected == True
    person.did_survive_infection(simulation.mortality_rate)
    assert person.is_alive == False
