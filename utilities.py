from dataclasses import dataclass
import numpy as np
import random
from math import inf
import copy



class Data:

    def __init__(self, number_of_nurses_, number_of_rooms_):
        self.number_of_rooms = number_of_rooms_
        self.number_of_nurses = number_of_nurses_
        self.next_id_nurse = 0
        self.next_id_room = 0
        self.nurses = []
        self.rooms = []
        self.wage = random.randint(20, 25)


        for i in range(self.number_of_nurses):
            self.add_nurse()
        for i in range(self.number_of_rooms):
            self.add_room()

    def add_nurse(self):
        self.nurses.append(Nurse(self.next_id_nurse))
        self.next_id_nurse += 1

    def add_room(self):
        self.rooms.append(Room(self.next_id_room))
        self.next_id_room += 1

    def print_nurses(self):
        for i in self.nurses:
            print("Nurse: ", i.id, ", status: ", i.status, ", worked hours: ", i.number_of_hours, ', salary: ', i.salary)

    def print_room(self):
        for i in self.rooms:
            print("Room: ", i.id, ", priority: ", i.priority)

class Nurse:

    def __init__(self, next_id):
        self.status = random.randint(1,5)
        self.id = next_id
        self.number_of_hours = 0
        self.salary = 0



class Room:
    def __init__(self, next_id):
        self.priority = random.randint(1,2)
        self.id = next_id

        if self.priority == 1:
            self.needed_number_of_nurses = 1
        else:
            self.needed_number_of_nurses = 2